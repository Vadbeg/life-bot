"""News parser based on RSS"""

import datetime

import dateutil.parser
import feedparser

from life_bot.news.news import PieceOfNews
from life_bot.news.utils import fix_ssl


class NewsParserURL:
    def __init__(self):
        pass

    def get_news_by_url(self, url: str) -> list[PieceOfNews]:
        fix_ssl()

        raw_feed = feedparser.parse(url_file_stream_or_string=url).entries
        news = self._parse_news(raw_feed=raw_feed)

        return news

    @staticmethod
    def _parse_news(raw_feed: dict) -> list[PieceOfNews]:
        news: list[PieceOfNews] = []
        for entry in raw_feed:
            published_date = dateutil.parser.parse(entry.published)

            piece_of_news = PieceOfNews(
                title=entry.title,
                link=entry.link,
                description=entry.description,
                date=published_date,
            )
            news.append(piece_of_news)

        return news
