# YouTube MP3 Downloader

## Description

A simple and efficient command-line tool to download MP3 audio files from YouTube videos, playlists, and channels. This tool uses `yt-dlp` for downloading, `ffmpeg` for audio conversion, and `tqdm` for progress visualization. It supports downloading multiple videos concurrently with a clean and user-friendly interface.

### Features:
- Download audio from single videos, playlists, or channels.
- Convert downloaded audio to MP3 format (192kbps).
- Optionally download video thumbnails and embed metadata.
- Multi-threaded downloading for faster processing.
- Customizable save location for downloaded files.
- Clear and stylish terminal interface with progress bars.

## Requirements
- Python 3.6+
- `yt-dlp`
- `ffmpeg`
- `tqdm`
- `colorama`
- `pyfiglet`

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/youtube-mp3-downloader.git
   cd youtube-mp3-downloader
   ```
   
2. Make sure you have `ffmpeg` installed and accessible in your system's PATH.

3. Download and install `yt-dlp` , `colorama` , `pyfiglet` and `tqdm` :

   ```bash
   pip install yt-dlp colorama tqdm pyfiglet
   ```

### Usage

1. Run the script:

   ```bash
   python youtube_mp3_downloader.py
   ```

2. You will be prompted to input:
   - The YouTube video, playlist, or channel URL.
   - The directory name where the MP3 files should be saved (optional).

3. The program will fetch the video URLs and start downloading the MP3 files to the specified directory.

4. Once the download is complete, you'll see a message indicating success.

### Example:

```bash
Video/Playlist/Channel URL: https://www.youtube.com/playlist?list=PLxKrR3VjggMv5oYFeOBtQzPimH8mMlhzI
Directory Name: My_Music
```

### Notes:
- If downloading a playlist or channel, the program will download MP3s for all the videos in the list.
- Make sure that `ffmpeg.exe` is installed and the path is correctly set in the script (`FFMPEG_PATH`).

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgements
- Thanks to [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the video downloading functionality.
- Thanks to [ffmpeg](https://ffmpeg.org/) for audio conversion capabilities.
- Thanks to [pyfiglet](https://github.com/pwaller/pyfiglet) for the banner text.
