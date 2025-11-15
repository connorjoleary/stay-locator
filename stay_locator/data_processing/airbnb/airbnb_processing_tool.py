import re

from stay_locator.common.origin import Origin
from stay_locator.data_processing.data_processing import DataProcessingTool


class AirBNBProcessingTool(DataProcessingTool):
    # TODO: may be able to make generic
    def convert_data_to_origin(self, simplified_data: dict[str, str]) -> Origin:
        price_raw = simplified_data["price"]
        price_clean = re.match(r"\$(\d+\.?\d*)", price_raw).group(1)
        rating_raw = simplified_data["avgRatingLocalized"]
        rating_clean = 0 if rating_raw == "New" else re.match(r"\d\.\d\d?", rating_raw).group(0)
        beds_raw = simplified_data["beds"]
        beds_clean = beds_raw[0] if isinstance(beds_raw, list) and len(beds_raw) == 1 else beds_raw
        return Origin(
            name=simplified_data["name"],
            id=simplified_data["propertyId"],
            location=(simplified_data["latitude"], simplified_data["longitude"]),
            metadata=simplified_data,
            price=int(price_clean),
            bedrooms=beds_clean,
            size=None,
            rating=float(rating_clean),
        )

    @property
    def important_data(self) -> list[any]:
        return [
            ("propertyId", ["data", "list", "listing", "id"]),
            ["data", "list", "listing", "name"],
            ["data", "list", "listing", "title"],
            ["data", "list", "listing", "roomTypeCategory"],
            ["data", "list", "listing", "city"],
            ["data", "list", "listing", "coordinate", "latitude"],
            ["data", "list", "listing", "coordinate", "longitude"],
            [
                "data",
                "list",
                "pricingQuote",
                "structuredStayDisplayPrice",
                "secondaryLine",
                "price",
            ],
            ["data", "list", "listing", "avgRatingLocalized"],
            ["data", "list", "listing", "roomTypeCategory"],
            (
                "beds",
                ["data", "list", "listing", "structuredContent", "primaryLine", "body", 0],
            ),
        ]
