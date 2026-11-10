"""YouTube transcripts -> 60-second chunks with timestamped links, ready for embeddings."""
import json
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fujiwaranosai/youtube-transcript-scraper").call(run_input={
    "videos": ["https://www.youtube.com/watch?v=aircAruvnKk"],
    "languages": ["en"],
    "outputFormat": "segments",
})


def chunks(segments, seconds=60):
    buf, start = [], segments[0]["start"]
    for s in segments:
        buf.append(s["text"])
        if s["start"] - start >= seconds:
            yield start, " ".join(buf)
            buf, start = [], s["start"]
    if buf:
        yield start, " ".join(buf)


docs = []
for video in client.dataset(run["defaultDatasetId"]).iterate_items():
    for start, text in chunks(video["segments"]):
        docs.append({"text": text, "source": f'https://youtu.be/{video["video_id"]}?t={int(start)}', "title": video["title"]})
print(json.dumps(docs[:3], indent=2, ensure_ascii=False))
print(f"{len(docs)} chunks")
