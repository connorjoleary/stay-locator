from abc import ABC, abstractmethod
from os import environ

import requests

from stay_locator.data_collection.common.utils import QueryDetails


class APITool(ABC):
    @property
    @abstractmethod
    def host(self):
        pass

    @property
    @abstractmethod
    def path(self):
        pass

    def __init__(self):
        if not self.host or not self.path:
            value_msg = "Requires host and path"
            raise ValueError(value_msg)
        self.url = f"https://{self.host}{self.path}"

    @abstractmethod
    def generate_query_string(self, query_details: QueryDetails) -> str:
        raise NotImplementedError

    def grab_raw_data(self, query_details: QueryDetails):
        query_string = self.generate_query_string(query_details)
        headers = {"X-RapidAPI-Key": environ["API_KEY"], "X-RapidAPI-Host": self.host}
        response = requests.get(self.url, headers=headers, params=query_string, timeout=10)
        return response.json()
