import yt_dlp
import os

def download_youtube_audio(youtube_url, audio_format='mp3', output_path='.'):
    """
    Downloads the audio from a YouTube video and converts it to the specified format.

    Args:
        youtube_url (str): The URL of the YouTube video.
        audio_format (str): The desired audio format (e.g., 'mp3', 'wav', 'm4a', 'aac', 'flac', 'opus').
                            Defaults to 'mp3'.
        output_path (str): The directory where the audio file will be saved.
                           Defaults to the current directory.
    """
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)
        print(f"Created output directory: {output_path}")

    # yt-dlp options for audio extraction and conversion
    ydl_opts = {
        'format': 'bestaudio/best',  # Select the best audio quality
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,  # Preferred audio codec
            'preferredquality': '192',       # Audio quality (e.g., 192kbps)
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'), # Output file name template
        'noplaylist': True,  # Only download the single video, not a playlist
        'ignoreerrors': True, # Continue on download errors
        'logtostderr': False, # Don't log to stderr
        'quiet': False,      # Show progress
        'no_warnings': False, # Show warnings
    }

    print(f"\nAttempting to download audio from: {youtube_url}")
    print(f"Desired format: {audio_format}")
    print(f"Saving to: {output_path}")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(youtube_url, download=True)
            # The actual file path after download and conversion
            # yt-dlp automatically handles naming and extensions based on 'outtmpl'
            # and 'postprocessors'. We can try to infer the final path.
            # This part can be tricky as yt-dlp's internal naming can vary.
            # A more robust way might be to list files in the output_path after download.
            
            # For simplicity, let's assume it names it based on title and preferred ext
            video_title = info_dict.get('title', 'downloaded_audio')
            final_filename = f"{video_title}.{audio_format}"
            print(f"Successfully downloaded and converted: {final_filename}")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure FFmpeg is installed and accessible in your system's PATH.")
        print("Also, check if the YouTube URL is valid and accessible.")

if __name__ == "__main__":
    print("--- YouTube Audio Downloader ---")
    print("Supported audio formats: mp3, wav, m4a, aac, flac, opus, etc.")

    while True:
        youtube_link = input("\nEnter the YouTube video URL (or 'q' to quit): ").strip()
        if youtube_link.lower() == 'q':
            break

        if not youtube_link:
            print("URL cannot be empty. Please try again.")
            continue

        desired_format = input("Enter the desired audio format (e.g., mp3, wav, m4a): ").strip().lower()
        if not desired_format:
            print("Audio format cannot be empty. Defaulting to 'mp3'.")
            desired_format = 'mp3'

        # You can specify a custom output directory here, or leave it as default (current folder)
        output_directory = "downloaded_audio" 
        
        download_youtube_audio(youtube_link, desired_format, output_directory)

    print("\nThank you for using the YouTube Audio Downloader!")

