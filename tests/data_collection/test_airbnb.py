import json
from datetime import date

import responses
from pytest import fixture

from stay_locator.data_collection.airbnb.airbnb_api_tool import AirBNBAPITool
from stay_locator.data_collection.common.utils import QueryDetails

AIRBNB_SEARCH_BY_LOC_PATH = "tests/test_data/rapid_api_examples/airbnb_search_by_loc.json"


class TestAirbnbDataCollection:
    @fixture
    def api_tool(self):
        return AirBNBAPITool()

    def test_simple_query_string(self, api_tool):
        query_details = QueryDetails(
            location="London",
            adults=2,
            checkIn=date(2024, 4, 13),
            checkOut=date(2024, 4, 15),
        )
        query_string = api_tool.generate_query_string(query_details)
        assert query_string == {"location": "London", "checkIn": "2024-04-13", "checkOut": "2024-04-15", "adults": "2"}

    @responses.activate
    def test_grab_data_happypath(self, api_tool):
        with open(AIRBNB_SEARCH_BY_LOC_PATH) as f:
            responses.get(
                api_tool.url,
                json=json.load(f),
            )

        query_details = QueryDetails(
            location="London",
            adults=2,
            checkIn=date(2024, 4, 13),
            checkOut=date(2024, 4, 15),
        )
        raw_data = api_tool.grab_raw_data(query_details)
        assert raw_data
