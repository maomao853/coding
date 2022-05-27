from dataclasses import dataclass, field

@dataclass
class Applicant:
    name: str = field(default="")
    positions: list = field(default_factory=list)
