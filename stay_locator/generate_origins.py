from stay_locator.data_collection.airbnb.airbnb_api_tool import AirBNBAPITool
from stay_locator.data_collection.common.utils import OriginSources, QueryDetails
from stay_locator.data_processing.airbnb.airbnb_processing_tool import AIRBNBProcessingTool


def generate_origins(query_details: QueryDetails, origin_sources: OriginSources) -> dict[str, OriginSources]:
    origins = {}

    # Airbnb
    if origin_sources.airbnb:
        airbnb_api_tool = AirBNBAPITool()
        airbnb_raw_data = airbnb_api_tool.grab_raw_data(query_details=query_details)
        # TODO: airbnb_processing_tool
        airbnb_processing_tool = AIRBNBProcessingTool()
        airbnb_origins = airbnb_processing_tool.process_raw_data(airbnb_raw_data)

        origins["airbnb"] = airbnb_origins

    # write_dataclasses(ORIGINS_FILENAME, origins, Origin)
    return origins
