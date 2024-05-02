import feedparser

# URL of The Verge's tech RSS feed
feed_url = 'https://www.theverge.com/rss/index.xml'

# Parse the feed
feed = feedparser.parse(feed_url)

# List the latest tech news
for entry in feed.entries[:10]:  # This limits the output to the latest 10 entries
    print(f"Title: {entry.title}")
    print(f"Link: {entry.link}")
    print(f"Published Date: {entry.published}")
    print('---')

# Display the custom message after listing the news
print("Made By WilsonRIP")

# Keep the window open until the user decides to close it
input("Press Enter to exit...")