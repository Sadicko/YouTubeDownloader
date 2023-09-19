import argparse
from pytube import YouTube, Playlist


def download_single_video(video_url):
    yt = YouTube(video_url, on_progress_callback=on_progress)
    video_stream = yt.streams.get_highest_resolution()
    print(f"Downloading: {yt.title}")
    video_stream.download()
    print(f"Downloaded: {yt.title}")


def download_playlist(playlist_url):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        yt = YouTube(video_url, on_progress_callback=on_progress)
        video_stream = yt.streams.get_highest_resolution()
        print(f"Downloading: {yt.title}")
        video_stream.download()
        print(f"Downloaded: {yt.title}")


def on_progress(stream, chunk, bytes_remaining):
    total_bytes = stream.filesize
    bytes_downloaded = total_bytes - bytes_remaining
    percentage = (bytes_downloaded / total_bytes) * 100
    print(f"Progress: {percentage:.2f}%   ", end='\r')


def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos or playlists.")
    parser.add_argument("-s", "--single", help="Download a single YouTube video. Provide the video URL.", type=str)
    parser.add_argument("-p", "--playlist", help="Download a YouTube playlist. Provide the playlist URL.", type=str)
    args = parser.parse_args()

    if args.single:
        download_single_video(args.single)
    elif args.playlist:
        download_playlist(args.playlist)
    else:
        print("Welcome to YouTube Downloader Script. You can download a single video or whole Playlist.")
        # If no command-line arguments are provided, ask the user for input.
        user_input = input("Enter a YouTube video or playlist URL: ")
        if user_input.startswith("https://www.youtube.com/watch?v="):
            download_single_video(user_input)
        elif user_input.startswith("https://www.youtube.com/playlist?list="):
            download_playlist(user_input)
        else:
            print("Invalid URL. Please provide a valid YouTube video or playlist URL.")


if __name__ == "__main__":
    main()
