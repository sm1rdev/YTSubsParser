from youtube_transcript_api import YouTubeTranscriptApi

video_id = "hP06ir896G8"

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)

for snippet in fetched_transcript:
    snippet_ms = int((snippet.start - int(snippet.start)) * 1000)
    snippet_s = int(snippet.start % 60)
    snippet_m = int(snippet.start / 60) if snippet.start > 60 else 0
    snippet_h = int(snippet.start / 3600) if snippet.start > 3600 else 0

    print(f"{snippet_h:02d}:{snippet_m:02d}:{snippet_s:02d},{snippet_ms:03d} : {snippet.text}")

