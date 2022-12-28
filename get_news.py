from life_bot.news import NewsAggregator

if __name__ == "__main__":
    urls = [
        "https://www.theguardian.com/world/rss",
        "https://www.theguardian.com/uk/rss",
        "https://vas3k.ru/rss",
    ]

    news_aggregator = NewsAggregator(urls=urls)
    news_by_feed = news_aggregator.get_news_by_url()

    print(news_by_feed)
