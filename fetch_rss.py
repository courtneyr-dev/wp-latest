import feedparser
from datetime import datetime, timedelta
import os

# List of RSS feeds
rss_feeds = {
    "WordPress News": "http://WordPress.org/news/rss",
    # Add more RSS feeds here
}

# Get date 7 days ago
date_limit = datetime.now() - timedelta(days=7)

def fetch_feed_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        published = datetime(*entry.published_parsed[:6])
        if published > date_limit:
            articles.append((entry.title, entry.link))
    return articles

markdown_content = ""
for title, url in rss_feeds.items():
    articles = fetch_feed_articles(url)
    if articles:
        markdown_content += f"## {title}\n"
        for article_title, article_link in articles:
            markdown_content += f"- [{article_title}]({article_link})\n"

# Save to a Markdown file
with open('ARTICLES.md', 'w') as file:
    file.write(markdown_content)
