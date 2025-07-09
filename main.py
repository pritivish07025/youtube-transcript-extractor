from youtube_transcript_api import YouTubeTranscriptApi

try:
    #video_id = "QXX2ySfwEBM"  # Example video ID
    #replace with your own video ID


    video_id = "QXX2ySfwEBM"

    # Try fetching English subtitles (auto-generated)
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

    text = " ".join([line['text'] for line in transcript])

    print("\n Transcript (english):\n")
    print(text)

except Exception as e:
    print(" Error:", e)

