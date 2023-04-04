# VideoMetadata
This Python script, named videometadata.py, extracts metadata from audio or video files in different formats, such as MP3, MP4, OGG, WAV, and WEBM. It uses the mutagen library to read the metadata from the file, and then handles the metadata according to the format of the file.

The script takes a command-line argument, which is the path to the audio or video file to extract metadata from. It then determines the file extension of the specified file, and calls a specific function to handle the metadata extraction, depending on the file format.

For MP3 files, the handle_id3 function is called, which extracts the ID3 tags from the file and prints them in a tabular format. For MP4 files, the handle_mp4 function is called, which extracts the QuickTime tags from the file and prints them in a tabular format. For OGG files, the handle_ogg function is called, which extracts the Vorbis tags from the file and prints them in a tabular format. For WAV files, the handle_wav function is called, which extracts the Wave tags from the file and prints them in a tabular format. For WEBM files, the handle_webm function is called, which extracts the WebM tags from the file and prints them in a tabular format.

To use the script, you need to have Python installed on your system and the mutagen library installed. You can run the script from the command line by typing "python videometadata.py <file_path>", where "<file_path>" is the path to the audio or video file to extract metadata from. The script will then print the metadata to the console.
