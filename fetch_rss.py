import feedparser
from datetime import datetime, timedelta
import os

# List of RSS feeds
rss_feeds = {
    "WordPress News": "http://wordpress.org/news/feed",
    "Accessibility": "https://make.wordpress.org/accessibility/feed",
    "CLI": "https://make.wordpress.org/cli/feed",
    "Community": "https://make.wordpress.org/community/feed",
    "Core": "https://make.wordpress.org/core/feed",
    "Core Dev Blog": "https://developer.wordpress.org/news/feed",
    "Design": "https://make.wordpress.org/design/feed",
    "Docs": "https://make.wordpress.org/docs/feed",
    "User Support Articles": "https://wordpress.org/support/articles/feed",
    "Developer Support Articles": "https://developer.wordpress.org/feed/?post_type%5B0%5D=wporg_explanations&amp;post_type%5B1%5D=apis-handbook&amp;post_type%5B2%5D=plugin-handbook&amp;post_type%5B3%5D=theme-handbook&amp;post_type%5B4%5D=blocks-handbook&amp;post_type%5B5%5D=wpcs-handbook&amp;post_type%5B6%5D=rest-api-handbook&amp;post_type%5B7%5D=wp-parser-function&amp;post_type%5B8%5D=wp-parser-class&amp;post_type%5B9%5D=wp-parser-hook&amp;post_type%5B10%5D=wp-parser-method&amp;post_type%5B11%5D=command",
    "Five for the Future": "https://openrss.org/github.com/wordpress/five-for-the-future/issues",
    "Hosting": "https://make.wordpress.org/hosting/feed",
    "Jobs": "https://jobs.wordpress.net/feed",
    "Marketing": "https://make.wordpress.org/marketing/feed",
    "Meta": "https://make.wordpress.org/meta/feed",
    "Playgrounds": "https://openrss.org/github.com/WordPress/wordpress-playground/issues",
    "Showcase": "https://openrss.org/github.com/WordPress/wporg-showcase-2022/issues",
    "WP org theme": "https://openrss.org/github.com/WordPress/wporg-main-2022/issues",
    "Mobile": "https://make.wordpress.org/mobile/feed",
    "Openverse": "https://make.wordpress.org/openverse/feed",
    "Performance": "https://make.wordpress.org/performance/feed",
    "Photos": "https://make.wordpress.org/photos/feed/",
    "Polyglots": "https://make.wordpress.org/polyglots/feed",
    "Plugins": "https://make.wordpress.org/plugins/feed",
    "Project": "https://make.wordpress.org/project/feed",
    "Security": "https://make.wordpress.org/security/feed",
    "Summit": "https://make.wordpress.org/summit/feed",
    "Support": "https://make.wordpress.org/support/feed",
    "Sustainability": "https://make.wordpress.org/sustainability/feed",
    "Summit": "https://make.wordpress.org/summit/feed",
    "Systems": "https://make.wordpress.org/systems/feed",
    "Test": "https://make.wordpress.org/test/feed",
    "Themes": "https://make.wordpress.org/themes/feed",
    "Tide": "https://make.wordpress.org/tide/feed",
    "Training": "https://make.wordpress.org/training/feed",
    "LearnWP": "htttps://learn.wordpress.org/feed",
    "LearnWP Lesson Plan": "https://learn.wordpress.org/feed/?post_type=lesson-plan",
    "LearnWP Tutorials": "https://learn.wordpress.org/feed/?post_type=wporg_workshop",
    "LearnWP Courses": "https://learn.wordpress.org/feed/?post_type=course",
    "LearnWP Online Workshops": "https://learn.wordpress.org/feed/?post_type=meeting",
    "TV": "https://make.wordpress.org/tv/feed",
    "WPTV": "https://wordpress.tv/feed/",
    "Updates": "https://make.wordpress.org/updates/feed",
    "WordCamp Central": "https://central.wordcamp.org/news/feed",
    "WordPress Foundation": "https://wordpressfoundation.org/feed/",
    "WordCamp": "https://central.wordcamp.org/wordcamps/feed/",
    "DoAction": "https://doaction.org/event/feed/",
    "WP20": "https://wp20.wordpress.net/feed",
}

# Get date 7 days ago
date_limit = datetime.now() - timedelta(days=14)

# Function to fetch articles from the feed
def fetch_feed_articles(feed_url):
    feed = feedparser.parse(feed_url)
    articles = []
    for entry in feed.entries:
        published = datetime(*entry.published_parsed[:6])
        if published > date_limit:
            articles.append((entry.title, entry.link))
    return articles

# Function to check if the article is already in the file
def is_article_already_added(article_title, file_content):
    return article_title in file_content


# Check if ARTICLES.md exists, if not, create it
if not os.path.exists('ARTICLES.md'):
    with open('ARTICLES.md', 'w'): pass

# Read the existing content of ARTICLES.md to avoid duplicating entries
existing_content = ""
if os.path.isfile('ARTICLES.md'):
    with open('ARTICLES.md', 'r') as file:
        existing_content = file.read()

markdown_content = ""
for title, url in rss_feeds.items():
    articles = fetch_feed_articles(url)
    if articles:
        markdown_content += f"## {title}\n"
        for article_title, article_link in articles:
            # Append only new articles
            if not is_article_already_added(article_title, existing_content):
                markdown_content += f"- [{article_title}]({article_link})\n"

# Append to the ARTICLES.md file
if markdown_content.strip() != "":
    with open('ARTICLES.md', 'a') as file:
        file.write(markdown_content)
