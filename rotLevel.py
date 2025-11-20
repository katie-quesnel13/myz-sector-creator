from dataclasses import dataclass, field
from typing import List, Any, Optional
from utitlityFunctions import *

@dataclass
class RotLevel:
    name: str
    level: int
    chance: int

ROT_LEVELS: List[RotLevel] = [
    RotLevel("Rot Oasis", 0, 2),
    RotLevel("Weak Rot", 1, 27),
    RotLevel("Rot-Heavy Area", 2, 7),
]

def set_rot_level() -> RotLevel:
    chosen = random.choices(
        ROT_LEVELS,
        weights=[rot.chance for rot in ROT_LEVELS],
        k=1
    )[0]
    return RotLevel(
        chosen.name,
        chosen.level,
        chosen.chance
    )