"""New 1-2 star reviews mentioning crashes or login problems, from both stores and two countries."""
import os
from collections import Counter

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fujiwaranosai/app-reviews-scraper").call(run_input={
    "apps": ["https://apps.apple.com/us/app/spotify/id324684580", "play:com.spotify.music"],
    "countries": ["us", "gb"],
    "maxRating": 2,
    "keywords": ["crash", "login", "freez"],
    "onlyNew": True,
})
reviews = list(client.dataset(run["defaultDatasetId"]).iterate_items())
print(f"{len(reviews)} new complaints")
print("by app version:", Counter(r["app_version"] for r in reviews).most_common(5))
for r in reviews[:20]:
    print(f'[{r["store"]}/{r["country"]}] {r["rating"]}★ v{r["app_version"]}: {(r["text"] or "")[:140]}')
