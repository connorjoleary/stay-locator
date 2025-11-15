import json

from pytest import fixture

from stay_locator.data_processing.airbnb.airbnb_processing_tool import AirBNBProcessingTool

AIRBNB_SEARCH_BY_LOC_PATH = "tests/test_data/rapid_api_examples/airbnb_search_by_loc.json"


class TestAirbnbDataProcessing:
    @fixture
    def api_tool(self):
        return AirBNBProcessingTool()

    def test_process_raw_data(self, api_tool):
        with open(AIRBNB_SEARCH_BY_LOC_PATH) as f:
            raw_data = json.load(f)

        origins = api_tool.process_raw_data(raw_data)
        assert len(origins) == 10
