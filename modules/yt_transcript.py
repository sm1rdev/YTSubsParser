from youtube_transcript_api import YouTubeTranscriptApi
import youtube_transcript_api._errors as ERRORS


ytt_api = YouTubeTranscriptApi()

def get_video_transcript(url):
    video_id = url.split("v=")[1].split("&")[0]

    try:
        transcript_list = ytt_api.list(video_id)

        for transcript in transcript_list:
            language_code = transcript.language_code

            try:
                fetched_transcript = transcript.fetch()
                transcript_data = format_transcript(fetched_transcript, video_id, language_code)
                return transcript_data
            except Exception as e:
                print(f"Ошибка при получении субтитров: {e}")
                return None

    except ERRORS.TranscriptsDisabled as e:
        print("Субтитры отключены")
        return None
    except ERRORS.NoTranscriptFound as e:
        print("Субтитры не найдены")
        return None
    except Exception as e:
        print(e)
        return None

def format_transcript(transcript, video_id, language_code):
    transcript_data = [video_id, language_code]

    for snippet in transcript:
        snippet_ms = int((snippet.start - int(snippet.start)) * 1000)
        snippet_s = int(snippet.start % 60)
        snippet_m = int(snippet.start / 60) if snippet.start > 60 else 0
        snippet_h = int(snippet.start / 3600) if snippet.start > 3600 else 0

        # print(f"{snippet_h:02d}:{snippet_m:02d}:{snippet_s:02d},{snippet_ms:03d} : {snippet.text}")
        transcript_data.append(f"{snippet_h:02d}:{snippet_m:02d}:{snippet_s:02d},{snippet_ms:03d} : {snippet.text}")

    return transcript_data
