from __future__ import print_function
import argparse
import json
import mutagen

def handle_id3(id3_file):
    id3_frames = {'TIT2': 'Title', 'TPE1': 'Artist', 'TALB': 'Album', 'TXXX': 'Custom', 'TCON': 'Content Type', 'TDRL': 'Date released', 'COMM': 'Comments', 'TDRC': 'Recording Date'}
    print("{:15} | {:15} | {:38} | {}".format("Frame", "Description","Text","Value"))
    print("-" * 85)
    
    for frames in id3_file.tags.values():
        frame_name = id3_frames.get(frames.FrameID, frames.FrameID)
        desc = getattr(frames, 'desc', "N/A")
        text = getattr(frames, 'text', ["N/A"])[0]
        value = getattr(frames, 'value', "N/A")
        
        if "date" in frame_name.lower():
            text = str(text)
        print("{:15} | {:15} | {:38} | {}".format(frame_name, desc, text, value))

def handle_mp4(mp4_file):
    cp_sym = u"\u00A9"
    qt_tag = {
        cp_sym + 'nam': 'Title', cp_sym + 'art': 'Artist', cp_sym + 'alb': 'Album', cp_sym + 'gen': 'Genre', 'cpil': 'Compilation', cp_sym + 'day': 'Creation Date', 'cnID': 'Apple Store Content ID', 'atID': 'Album Title ID', 'plID': 'Playlist ID', 'geID': 'Genre ID', 'pcst': 'Podcast', 'purl': 'Podcast URL', 'egid': 'Episode Global ID', 'cmID': 'Camera ID', 'sfID': 'Apple Store Country', 'desc': 'Description', 'ldes': 'Long Description'
    }
    genre_ids = json.load(open('apple_genres.json'))

    print("{:22} | {}".format('Name', 'Value'))
    print("-" * 40)

    for name, value in mp4_file.tags.items():
        tag_name = qt_tag.get(name, name)

        if isinstance(value, list):
            value = "; ".join([str(x) for x in value])
        if name == 'geID':
            value = "{}: {}".format(value, genre_ids.get(str(value), "Unknown genre").replace("|", " - "))
        print("{:22} | {}".format(tag_name, value))

def handle_ogg(ogg_file):
    ogg_tags = {'title': 'Title', 'artist': 'Artist', 'album': 'Album', 'genre': 'Genre', 'date': 'Date released', 'comment': 'Comments'}
    print("{:15} | {:38} | {}".format("Tag", "Text", "Value"))
    print("-" * 65)

    for tag in ogg_file.tags:
        tag_name = ogg_tags.get(tag, tag)
        text = ogg_file[tag][0]
        value = text
        
        if "date" in tag_name.lower():
            text = str(text)
        print("{:15} | {:38} | {}".format(tag_name, text, value))

def handle_wav(wav_file):
    print("{:15} | {}".format('Name', 'Value'))
    print("-" * 30)
    for name, value in wav_file.tags.items():
        print("{:15} | {}".format(name, value[0]))

def handle_webm(webm_file):
    print("{:15} | {}".format('Name', 'Value'))
    print("-" * 30)
    for name, value in webm_file.tags.items():
        print("{:15} | {}".format(name, value))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Python Metadata Extractor')
    parser.add_argument("AV_FILE", help="File to extract metadata from")
    args = parser.parse_args()
    av_file = mutagen.File(args.AV_FILE)
    if av_file is None:
        print("Unable to extract metadata from the specified file.")
        exit()
    file_ext = args.AV_FILE.rsplit('.', 1)[-1].lower()

    if file_ext == 'mp3':
        handle_id3(av_file)
    elif file_ext == 'mp4':
        handle_mp4(av_file)
    elif file_ext == 'ogg':
        handle_ogg(av_file)
    elif file_ext == 'wav':
        handle_wav(av_file)
    elif file_ext == 'webm':
        handle_webm(av_file)
    else:
        print("Unsupported file format. Please specify an MP3 or MP4 file.")
