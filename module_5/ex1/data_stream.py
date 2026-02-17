#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class StreamErrors(Exception):
    pass


class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:

        if isinstance(stream_id, str) is False:
            raise StreamErrors("Error: stream_id must be a string")
        if not stream_id:
            raise StreamErrors("Error: stream_id cannot be empty")

        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        raise StreamErrors(
            "Error: filter_data not implemented for this stream"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"stream_id": self.stream_id}


class StreamProcessor:

    def run_stream(self, stream: Any, data: list[Any]) -> str:
        return stream.process_batch(data)

    def filter(self, stream: Any, criteria: str, data: list[Any]) -> list[Any]:
        return stream.filter_data(data, criteria)


class SensorStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Environmental Data"

    def process_batch(self, data_batch: List[Any]) -> str:

        filter = self.filter_data(data_batch, "temp")
        return (
            f"{len(data_batch)} readings processed, avg temp: "
            f"{sum(filter) / len(filter)}°C"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if not isinstance(data_batch, list) or len(data_batch) == 0:
            raise StreamErrors(
                "Error: invalid data_batch: expected non-empty list"
            )

        temps = list()
        if criteria == "temp":

            for data in data_batch:
                if isinstance(data, str) is False:
                    raise StreamErrors(
                        "Error: each item in data_batch must be a string"
                    )
                if data.count(":") != 1:
                    raise StreamErrors(
                        "Error: malformed sensor reading, expected 'key:value'"
                    )
            try:
                temps = [
                    float(data.split(":")[1])
                    for data in data_batch if data.split(":")[0] == "temp"
                ]
            except ValueError:
                raise StreamErrors(
                    "Error: sensor value must be numeric"
                )
            if len(temps) == 0:
                raise StreamErrors(
                    "Error: no temperature readings found in batch"
                )
            return temps

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"type": self.type})
        return stats


class TransactionStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "Financial Data"

    def process_batch(self, data_batch: List[Any]) -> str:

        filter = self.filter_data(data_batch, "high_tr")
        return (
            f"{len(data_batch)} operations, net flow: "
            f"{'+' if filter[0] > 0 else ''}{filter[0]} units"
        )

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if isinstance(data_batch, list) is False or len(data_batch) == 0:
            raise StreamErrors(
                "Error: invalid data_batch: expected non-empty list"
            )

        if criteria == "high_tr":
            buy = 0
            sell = 0
            for data in data_batch:
                if isinstance(data, str) is False:
                    raise StreamErrors(
                        "Error: each item in data_batch must be a string"
                    )
                if data.count(":") != 1:
                    raise StreamErrors(
                        "Error: malformed transaction entry, "
                        "expected 'key:value'"
                    )
            try:
                buy = sum(
                    [
                        int(data.split(":")[1])
                        for data in data_batch if data.split(":")[0] == "buy"
                    ]
                )
                sell = sum(
                    [
                        int(data.split(":")[1])
                        for data in data_batch if data.split(":")[0] == "sell"
                    ]
                )
            except ValueError:
                raise StreamErrors(
                    "Error: transaction value must be integer"
                )
            return [buy - sell]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"type": self.type})
        return stats


class EventStream(DataStream):

    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.type = "System Events"

    def process_batch(self, data_batch: List[Any]) -> str:

        filter = self.filter_data(data_batch, "error")
        return f"{len(data_batch)} events, " f"{filter[0]} error detected"

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        if isinstance(data_batch, list) is False or len(data_batch) == 0:
            raise StreamErrors(
                "Error: invalid data_batch: expected non-empty list"
            )

        if len(data_batch) == 0:
            raise StreamErrors("Error: empty data batch")

        if criteria == "error":
            count = 0
            for data in data_batch:
                if isinstance(data, str) is False:
                    raise StreamErrors(
                        "Error: each item in data_batch must be a string"
                    )
                if data == "error":
                    count += 1
            return [count]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats.update({"type": self.type})
        return stats


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    sensor = SensorStream("SENSOR_001")
    try:
        print(
            f"Stream ID: {sensor.get_stats().get("stream_id")}, "
            f"Type: {sensor.get_stats().get("type")}"
        )
        data_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
        proc = sensor.process_batch(data_batch)
        print(f"Processing sensor batch: [{", ".join(data_batch)}]")
        print(f"Sensor analysis: {proc}")
    except StreamErrors as e:
        print(e)

    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    try:
        print(
            f"Stream ID: {transaction.get_stats().get("stream_id")}, "
            f"Type: {transaction.get_stats().get("type")}"
        )
        data_batch = ["buy:100", "sell:150", "buy:75"]
        proc = transaction.process_batch(data_batch)
        print(f"Processing transaction batch: [{", ".join(data_batch)}]")
        print(f"Transaction analysis: {proc}")
    except StreamErrors as e:
        print(e)

    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    try:
        print(
            f"Stream ID: {event.get_stats().get("stream_id")}, "
            f"Type: {event.get_stats().get("type")}"
        )
        data_batch = ["login", "error", "logout"]
        proc = event.process_batch(data_batch)
        print(f"Processing event batch: [{", ".join(data_batch)}]")
        print(f"Event analysis: {proc}")
    except StreamErrors as e:
        print(e)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    print("Batch 1 Results:")

    stream = StreamProcessor()
    sensor_data = ["temp:22.5", "humidity:65"]
    try:
        print(
            "- Sensor data: "
            f"{stream.run_stream(sensor, sensor_data).split(",")[0]}"
        )
    except StreamErrors as e:
        print(e)

    transaction_data = ["buy:100", "sell:150", "buy:75", "sell:20"]
    try:
        print(
            "- Transaction data: "
            f"{stream.run_stream(transaction, transaction_data).split(",")[0]}"
            " processed"
        )
    except StreamErrors as e:
        print(e)

    event_data = ["login", "error", "logout"]
    try:
        print(
            "- Event data: "
            f"{stream.run_stream(event, event_data).split(",")[0]}"
            " processed"
        )
    except StreamErrors as e:
        print(e)

    print("\nStream filtering active: High-priority data only")
    try:
        print(
            f"Filtered results: "
            f"{len(stream.filter(sensor, "temp", ["temp:20", "temp:35"]))} "
            "critical sensor alerts, "
            f"{len(stream.filter(transaction,
                                 "high_tr", ["sell:100", "buy:50"]))}"
            " large transaction"
        )
    except StreamErrors as e:
        print(e)

    print("\nAll streams processed successfully. Nexus throughput optimal.")
