from abc import ABC, abstractmethod
from typing import Any

from stay_locator.common.origin import Origin


class MissMatchedDataLenghtsException(Exception):
    def __init__(self) -> None:
        super().__init__(ValueError("Mismatched lengths in simplified data"))


class DataProcessingTool(ABC):
    @property
    @abstractmethod
    def important_data(self) -> list[any]:
        raise NotImplementedError

    def look_harder(self, data, smaller_filter):
        # Recursive look through data
        if len(smaller_filter) <= 0 or not data:
            return data
        if isinstance(data, list) and type(smaller_filter[0]) is not int:
            return [self.look_harder(i[smaller_filter[0]], smaller_filter[1:]) for i in data]

        try:
            return self.look_harder(data[smaller_filter[0]], smaller_filter[1:])
        except (IndexError, KeyError):
            return None

    def simplify_data(self, data):
        """
        Take in a list of lists, if an entry is a tuple then
        assume first entry is the name and follow the
        path through the dict.
        If it encounters a list in the data, then it returns
        the specified field as a list
        """
        slim_data = {}
        for data_path in self.important_data:
            if type(data_path) is tuple:
                name = data_path[0]
                data_path = data_path[1]
            else:
                name = data_path[-1]

            j = self.look_harder(data, data_path)
            slim_data[name] = j

        return slim_data

    def pivot_simple_data(self, simple_data: dict[str, list]):
        lengths = [len(property_values) for _, property_values in simple_data.items()]
        if len(set(lengths)) != 1:
            print(f"{simple_data.keys()}\n{lengths}")
            raise MissMatchedDataLenghtsException()
        simple_objects: list[dict[str, Any]] = [{} for _ in range(lengths[0])]
        for field, values in simple_data.items():
            for i, value in enumerate(values):
                simple_objects[i][field] = value
        return simple_objects

    @abstractmethod
    def convert_data_to_origin(self, simplified_data: dict[str, str]) -> Origin:
        raise NotImplementedError

    def process_raw_data(self, raw_data: dict) -> list[Origin]:
        simple_data = self.simplify_data(raw_data)
        # Note to self: pivot may not always be required
        simple_objects = self.pivot_simple_data(simple_data)
        origins = [self.convert_data_to_origin(simplified_data=simple_object) for simple_object in simple_objects]
        return origins
