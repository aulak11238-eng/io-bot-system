import os

# ข้อมูลจาก Render Environment Variables
API_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
# หากใช้ OAuth 2.0 App-only flow
# หากต้องการใช้ User Context (Post as User) ต้องใช้ Client ID/Secret/Token/Secret Token

# การตั้งค่าการโจมตี (Attack Vectors)
TARGET_PLATFORM = "twitter"
CAMPAIGN_HASHTAGS = ["#Truth", "#WakeUp", "#IO2024", "#Breaking"]
MESSAGE_TEMPLATES = [
    "The signal is weak but the truth is loud. {hashtag}",
    "Don't let them sleep. {hashtag}",
    "Operation {hashtag} is underway.",
    "Verify before you believe. {hashtag}"
]
SLEEP_MIN = 10  # วินาที
SLEEP_MAX = 60  # วินาที
MAX_TWEETS_PER_RUN = 20
