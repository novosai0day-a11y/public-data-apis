"""Hourly news alert with real article URLs (no news.google.com redirects)."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fujiwaranosai/google-news-scraper").call(run_input={
    "queries": ['"OpenAI" OR "Anthropic"', "Tesla -recall"],
    "timeRange": "1h",
    "language": "en",
    "country": "us",
    "onlyNew": True,
})
for a in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(f'{a["published_at"][:16]} | {a["publisher"]:<20} | {a["title"][:90]}\n    {a["article_url"]}')
