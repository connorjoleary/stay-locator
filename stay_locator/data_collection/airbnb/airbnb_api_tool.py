from stay_locator.data_collection.common.api_abstract import APITool
from stay_locator.data_collection.common.utils import QueryDetails


class AirBNBAPITool(APITool):
    @property
    def host(self):
        return "airbnb19.p.rapidapi.com"

    @property
    def path(self):
        return "/api/v1/searchPropertyByLocationV2"

    def generate_query_string(self, query_details: QueryDetails):
        # TODO: Handle checking of values (if required)
        query_string = {
            "location": query_details.location,
            "checkIn": query_details.checkIn.isoformat(),
            "checkOut": query_details.checkOut.isoformat(),
            "adults": str(query_details.adults),
        }
        if query_details.max_price:
            query_string["priceMax"] = str(query_details.max_price)
        return query_string
