# Public data APIs — ready-to-run examples

Small, practical examples for four data APIs (Apify Actors) I built and maintain. Each one reads **public** data, returns
clean JSON and is billed per result, so you can try them with the free Apify plan.

| Data | Actor | Example |
|---|---|---|
| Open jobs from Greenhouse, Lever, Ashby, Workable, SmartRecruiters, Recruitee | [ATS Jobs Feed](https://apify.com/fujiwaranosai/ats-jobs-feed) | [`examples/job_alerts.py`](examples/job_alerts.py) |
| App Store + Google Play reviews (ratings, text, version, replies) | [App Reviews Scraper](https://apify.com/fujiwaranosai/app-reviews-scraper) | [`examples/one_star_reviews.py`](examples/one_star_reviews.py) |
| YouTube transcripts / subtitles (any language, timestamps) | [YouTube Transcript Scraper](https://apify.com/fujiwaranosai/youtube-transcript-scraper) | [`examples/youtube_to_rag_chunks.py`](examples/youtube_to_rag_chunks.py) |
| Google News articles with the **real publisher URL** | [Google News Scraper](https://apify.com/fujiwaranosai/google-news-scraper) | [`examples/news_alert.py`](examples/news_alert.py) |

## Setup

```bash
pip install apify-client
export APIFY_TOKEN=...   # https://console.apify.com/settings/integrations
python examples/job_alerts.py
```

All four support an **only new results** mode: schedule them (Apify Schedules, cron, GitHub Actions) and you get alerts
instead of full dumps.

## Use cases

- Job alerts, hiring signals for sales, salary benchmarks
- Product feedback and competitor monitoring from app reviews
- RAG / summaries / content repurposing from YouTube videos
- Brand, competitor and market news monitoring in any country

Issues and ideas welcome — open an issue here or on the actor's page.
