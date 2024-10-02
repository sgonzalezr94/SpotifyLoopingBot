from dataclasses import dataclass, fields, field
from dotenv import load_dotenv
from os import environ
from json import loads


@dataclass
class BotSettings:
    login_url: str = ""
    driver_url: str = ""
    artist_url: str = ""
    window: str = ""
    username: str = ""
    password: str = ""
    buttons: dict = field(default_factory=dict)
    start_time: int = 15
    end_time: int = 35

    def __repr__(self) -> str:
        return self.__dict__

    def __str__(self) -> str:
        return str(self.__repr__())

    def __iter__(self):
        for field in fields(self):
            yield getattr(self, field.name)

    def load(self):
        load_dotenv(override=True)
        for attribute in self.__annotations__:
            if attribute == "buttons":
                self.__setattr__(attribute, loads(environ.get(attribute)))
            else:
                self.__setattr__(attribute, environ.get(attribute))
