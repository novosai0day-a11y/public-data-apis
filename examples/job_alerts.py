"""New remote data jobs at a list of companies (Greenhouse / Lever / Ashby / Workable / SmartRecruiters / Recruitee)."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("fujiwaranosai/ats-jobs-feed").call(run_input={
    "companies": ["greenhouse:stripe", "ashby:openai", "lever:palantir", "notion", "figma"],
    "keywords": ["data", "analytics", "machine learning"],
    "remoteOnly": True,
    "onlyNew": True,
    "includeDescription": False,
})
for job in client.dataset(run["defaultDatasetId"]).iterate_items():
    salary = f'{job["salary_min"]:,.0f}-{job["salary_max"]:,.0f} {job["salary_currency"]}' if job.get("salary_min") else ""
    print(f'{job["company"]:<12} {job["title"][:60]:<60} {job["location"] or "":<25} {salary} {job["url"]}')
