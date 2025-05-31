import modules.yt_dlp as yt_dlp
import modules.yt_transcript as yt_transcript
import modules.file_manager as file_manager

urls = file_manager.read_urls()

for url in urls:
    metadata = yt_dlp.get_video_metadata(url)
    transcript = yt_transcript.get_video_transcript(url)
    file_manager.create_file(metadata, transcript)