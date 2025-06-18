from dataclasses import dataclass


@dataclass
class Bill:
    value: float
    description: str
