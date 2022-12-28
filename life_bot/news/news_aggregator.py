"""Module with news aggregator"""

import os
from multiprocessing import Pool

from life_bot.news.news import PieceOfNews
from life_bot.news.news_parser import NewsParserURL


class NewsAggregator:
    def __init__(self, urls: list[str]):
        super().__init__()

        self._urls = urls

    def get_news_by_url(self) -> dict[str, list[PieceOfNews]]:
        news_parser = NewsParserURL()

        with Pool(processes=os.cpu_count()) as pool:
            news = pool.map(news_parser.get_news_by_url, self._urls)

        news_by_url = {}
        for curr_url, curr_news in zip(self._urls, news):
            news_by_url[curr_url] = curr_news

        return news_by_url
