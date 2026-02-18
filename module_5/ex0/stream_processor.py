#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional  # noqa


class ErrorManager(Exception):
    pass


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: list[int]) -> str:
        if self.validate(data):
            if isinstance(data, int):
                return (
                    f"Processed 1 numeric values, "
                    f"sum={data}, avg={data}"
                )
            else:
                return (
                    f"Processed {len(data)} numeric values, "
                    f"sum={sum(data)}, avg={sum(data)/len(data):.1f}"
                )

    def validate(self, data: list[int]) -> bool:

        if isinstance(data, int):
            return True

        if not isinstance(data, list):
            raise ErrorManager(
                "Error: Invalid data type: expected a list of numbers"
            )

        if len(data) == 0:
            raise ErrorManager("Error: Cannot process empty list")

        for elem in data:
            if isinstance(elem, int) is False:
                raise ErrorManager(
                    "Error: Invalid element: all items must be integers"
                )
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def process(self, data: str) -> str:
        if self.validate(data):
            return (
                f"Processed text: {len(data)} characters, "
                f"{len(data.split())} words"
            )

    def validate(self, data: str) -> bool:
        if isinstance(data, str) is False:
            raise ErrorManager("Error: Invalid data type: expected a string")
        elif not data:
            raise ErrorManager("Error: Cannot process empty text")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def process(self, data: str) -> str:
        if self.validate(data):
            log_level, flag = (
                ("[ALERT]", "ERROR") if "ERROR" in data else ("[INFO]", "INFO")
            )
            return (f"{log_level} {flag} level detected:"
                    f"{data.split(':')[1]}")

    def validate(self, data: str) -> bool:
        if isinstance(data, str) is False:
            raise ErrorManager(
                "Error: Invalid data type: expected a log entry string"
            )
        elif not data:
            raise ErrorManager("Cannot process empty log entry")
        elif (data.startswith("ERROR:") is False
              and data.startswith("INFO:") is False):
            raise ErrorManager(
                "Malformed log entry: expected 'LEVEL: message'"
            )
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    data: Union[List[int], int] = [1, 2, 3, 4, 5]
    num_obj: NumericProcessor = NumericProcessor()
    print(f"Processing data: {data}")
    try:
        if num_obj.validate(data):
            print("Validation: Numeric data verified")
        res: str = num_obj.process(data)
        print(num_obj.format_output(res))
    except ErrorManager as e:
        print(e)

    print("\nInitializing Text Processor...")
    data: str = "Hello Nexus World"
    text_obj: TextProcessor = TextProcessor()
    print(f'Processing data: "{data}"')
    try:
        if text_obj.validate(data):
            print("Validation: Text data verified")
        res: str = text_obj.process(data)
        print(text_obj.format_output(res))
    except ErrorManager as e:
        print(e)

    print("\nInitializing Log Processor...")
    data: str = "ERROR: Connection timeout"
    log_obj: LogProcessor = LogProcessor()
    print(f'Processing data: "{data}"')
    try:
        if log_obj.validate(data):
            print("Validation: Log entry verified")
        res: str = log_obj.process(data)
        print(log_obj.format_output(res))
    except ErrorManager as e:
        print(e)

    print("\n=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...")

    processors: list[DataProcessor] = [
        num_obj,
        text_obj,
        log_obj
    ]

    data_items: List[Any] = [
        [2, 3, 1],
        "Hello World!",
        "INFO: System ready"
    ]

    i: int = 0
    while i < len(processors):
        try:
            print(f"Result {i + 1}: {processors[i].process(data_items[i])}")
        except ErrorManager as e:
            print(e)
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
