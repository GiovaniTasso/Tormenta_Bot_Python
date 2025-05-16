from dataclasses import dataclass
from typing import Optional, List

@dataclass
class SpellEnhancement:
    cost: str
    description: str

@dataclass
class Spell:
    name: str
    level: int
    school: str
    casting_time: str
    range: str
    target: str
    duration: str
    resistance: str
    description: str
    type: str = ""  # Arcana, Divina, Universal
    enhancements: List[SpellEnhancement] = None

@dataclass
class Rule:
    name: str
    category: str
    description: str

@dataclass
class Power:
    name: str
    description: str
    requirements: str
    power_type: str  # "class", "race", "origin", "tormenta"
    class_name: Optional[str] = None  # For class powers
    race: Optional[str] = None  # For race powers
    origin: Optional[str] = None  # For origin powers
