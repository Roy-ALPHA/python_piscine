#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any


class AllErrors(Exception):
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
            return (
                f"Processed {len(data)} numeric values, "
                f"sum={sum(data)}, avg={sum(data)/len(data):.1f}"
            )

    def validate(self, data: list[int]) -> bool:
        if isinstance(data, list) is False:
            raise AllErrors("Error: Invalid data type: expected a list of numbers")

        if len(data) == 0:
            raise AllErrors("Error: Cannot process empty list")

        for elem in data:
            if isinstance(elem, int) is False:
                raise AllErrors("Error: Invalid element: all items must be integers")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):

    def process(self, data: str) -> str:
        if self.validate(data):
            return (
                f"Processed text: {len(data)} characters, " f"{len(data.split())} words"
            )

    def validate(self, data: str) -> bool:
        if isinstance(data, str) is False:
            raise AllErrors("Error: Invalid data type: expected a string")
        elif not data:
            raise AllErrors("Error: Cannot process empty text")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):

    def process(self, data: str) -> str:
        if self.validate(data):
            log_level, flag = (
                ("[ALERT]", "ERROR") if "ERROR" in data else ("[INFO]", "INFO")
            )
            return f"{log_level} {flag} level detected: " f"{data.split(":")[1]}"

    def validate(self, data: str) -> bool:
        if isinstance(data, str) is False:
            raise AllErrors("Error: Invalid data type: expected a log entry string")
        elif not data:
            raise AllErrors("Cannot process empty log entry")
        elif data.startswith("ERROR:") is False and data.startswith("INFO:") is False:
            raise AllErrors("Malformed log entry: expected 'LEVEL: message'")
        return True

    def format_output(self, result: str) -> str:
        return super().format_output(result)


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    print("\nInitializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    num_obj = NumericProcessor()
    print(f"Processing data: {data}")
    try:
        if num_obj.validate(data):
            print("Validation: Numeric data verified")
        res = num_obj.process(data)
        print(num_obj.format_output(res))
    except AllErrors as e:
        print(e)

    print("\nInitializing Text Processor...")
    data = "Hello Nexus World"
    text_obj = TextProcessor()
    print(f'Processing data: "{data}"')
    try:
        if text_obj.validate(data):
            print("Validation: Text data verified")
        res = text_obj.process(data)
        print(text_obj.format_output(res))
    except AllErrors as e:
        print(e)

    print("\nInitializing Log Processor...")
    data = "ERROR: Connection timeout"
    log_obj = LogProcessor()
    print(f'Processing data: "{data}"')
    try:
        if log_obj.validate(data):
            print("Validation: Log entry verified")
        res = log_obj.process(data)
        print(log_obj.format_output(res))
    except AllErrors as e:
        print(e)

    print("\n=== Polymorphic Processing Demo ===\n")

    print("Processing multiple data types through same interface...")

    data = [2, 3, 1]
    try:
        print(f"Result 1: {num_obj.process(data)}")
    except AllErrors as e:
        print(e)

    data = "Hello World!"
    try:
        print(f"Result 2: {text_obj.process(data)}")
    except AllErrors as e:
        print(e)

    data = "INFO: System ready"
    try:
        print(f"Result 3: {log_obj.process(data)}")
    except AllErrors as e:
        print(e)

    print("\nFoundation systems online. Nexus ready for advanced streams.")
