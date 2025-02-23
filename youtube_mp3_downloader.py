import yt_dlp
import os
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import Fore, Style, init
import time
import pyfiglet

# Initialize colorama
init(autoreset=True)

# Base download folder
BASE_DIR = Path("Music")
FFMPEG_PATH = r"ffmpeg.exe"

# Ensure the base directory exists
os.makedirs(BASE_DIR, exist_ok=True)

def show_banner():
    """Displays a text banner."""
    os.system('cls' if os.name == 'nt' else 'clear')
    ascii_text = pyfiglet.figlet_format("YouTube MP3 Downloader")
    print(Fore.CYAN + ascii_text + Style.RESET_ALL)
    time.sleep(2)

def get_video_urls(url):
    """Retrieves video URLs from a given YouTube URL (single video, playlist, or channel)."""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'force_generic_extractor': False
    }
    
    if "@" in url:  # Check if the URL is a channel link
        url += "/videos"  # Append /videos to get all uploaded videos
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            if 'entries' in info_dict:
                return [entry['url'] for entry in info_dict['entries'] if 'url' in entry]
            return [url]  # If it's a single video
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
            return []

def download_mp3(url, save_path):
    """Downloads an MP3 file from a given YouTube video URL."""
    save_path = Path(save_path)
    os.makedirs(save_path, exist_ok=True)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
            {'key': 'EmbedThumbnail'},
            {'key': 'FFmpegMetadata'},
        ],
        'ffmpeg_location': FFMPEG_PATH,
        'noplaylist': False,
        'writethumbnail': True,
        'outtmpl': str(save_path / '%(title)s.%(ext)s'),
        'quiet': True,
        'no_warnings': True,
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    show_banner()
    print(Fore.CYAN + "YouTube MP3 Downloader" + Style.RESET_ALL)
    url = input(Fore.YELLOW + "Video/Playlist/Channel URL: " + Style.RESET_ALL).strip()
    
    save_folder = input(Fore.YELLOW + "Directory Name: " + Style.RESET_ALL).strip()
    save_path = BASE_DIR / (save_folder if save_folder else "Downloads")
    
    video_urls = get_video_urls(url)
    if not video_urls:
        print(Fore.RED + "No videos found or invalid URL." + Style.RESET_ALL)
        return
    
    print(Fore.MAGENTA + "Downloading MP3 files..." + Style.RESET_ALL)
    with ThreadPoolExecutor() as executor:
        futures = {executor.submit(download_mp3, url, save_path): url for url in video_urls}
        for future in tqdm(as_completed(futures), total=len(futures), desc=Fore.GREEN + "Downloading" + Style.RESET_ALL, unit="audio"):
            try:
                future.result()
            except Exception as e:
                print(Fore.RED + f"Error downloading: {e}" + Style.RESET_ALL)
    
    print(Fore.CYAN + "Download complete!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
