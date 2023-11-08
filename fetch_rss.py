name: RSS Article Fetcher

on:
  schedule:
    - cron: '*/15 * * * *' # Runs every 15 minutes

jobs:
  fetch-rss:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'
        
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install feedparser
        
      - name: Fetch RSS Articles
        run: python fetch_rss.py
      
      - name: Commit and push if there are changes
        run: |
          git config --global user.email "action@github.com"
          git config --global user.name "GitHub Action"
          git add ARTICLES.md
          git commit -m "Updated articles list" -a || echo "No changes to commit"
          git push