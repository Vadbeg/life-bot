from dataclasses import dataclass
from datetime import datetime


@dataclass
class PieceOfNews:
    """Class for one piece of news"""

    title: str
    link: str
    description: str

    date: datetime = datetime.now()

    def __str__(self):
        return f"{self.title}\n{self.link}\n{self.description}"

    def __repr__(self):
        return f"{self.title}\n{self.link}\n{self.description}"

    def __eq__(self, other):
        return (
            self.title == other.title
            and self.link == other.link
            and self.description == other.description
        )

    def __hash__(self):
        return hash((self.title, self.link, self.description))


@dataclass
class NewsByFeed:
    """Class for news by feed"""

    feed: str
    news: list[PieceOfNews]
