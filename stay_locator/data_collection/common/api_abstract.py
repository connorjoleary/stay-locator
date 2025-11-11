from os import environ

import requests

from stay_locator.data_collection.common.utils import QueryDetails


# TODO: make abstract
class APITool:
    host = ""
    path = ""

    def __init__(self):
        if not self.host or not self.path:
            value_msg = "Requires host and path"
            raise ValueError(value_msg)
        self.url = f"https://{self.host}{self.path}"

    def generate_query_string(self, query_details: QueryDetails) -> str:
        raise NotImplementedError

    def grab_raw_data(self, query_details: QueryDetails):
        query_string = self.generate_query_string(query_details)
        headers = {"X-RapidAPI-Key": environ["API_KEY"], "X-RapidAPI-Host": self.host}
        response = requests.get(self.url, headers=headers, params=query_string, timeout=10)
        return response.json()
