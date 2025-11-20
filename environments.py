from dataclasses import dataclass, field
from typing import List, Any, Optional
from utitlityFunctions import *

@dataclass
class EnvironmentTemplate:
    name: str
    is_ruin: bool
    chance: int

@dataclass
class EnvironmentResult:
    name: str
    is_ruin: bool
    ruin_type: Optional[str]


RUIN_TYPES = [
    "Airplane Wreck", "Amusement Park", "Battlefield", "Bus Station", "Car Park", "Church", "Cinema", "Crater", "Dilapidated Mansion",
    "Fast Food Joint", "Gas Station", "Highway", "Hospital", "Hunting Store", "Mall", "Marina", "Museum", "Office Building",
    "Overgrown Park", "Playground", "Police Station", "Radio Station", "Residential Blocks", "Road Tunnel", "Ruined Bridge",
    "School", "Shelter", "Skyscraper", "Sports Center", "Suburbia", "Subway Station", "Supermarket", "Swimming Hall",
    "Tank", "Theater", "Train Station", "Factory", "Military Base", "Oil Cistern", "Pipeline", "Purification Plant", "Power Line",
    "Radio Mast", "Refinery", "Rubbish Dump", "Shipwreck", "Shooting Range", "Windmill"
]

ENVIRONMENTS: List[EnvironmentTemplate] = [
    EnvironmentTemplate("Thick Woods", False, 2),
    EnvironmentTemplate("Scrublands", False, 3),
    EnvironmentTemplate("Marshlands", False, 2),
    EnvironmentTemplate("Dead Woods", False, 3),
    EnvironmentTemplate("Ash Desert", False, 2),
    EnvironmentTemplate("Huge Crater", False, 1),
    EnvironmentTemplate("Glassified Field", False, 1),
    EnvironmentTemplate("Overgrown Ruins", True, 3),
    EnvironmentTemplate("Crumbling Ruins", True , 3),
    EnvironmentTemplate("Decayed Ruins", True , 5),
    EnvironmentTemplate("Unscathed Ruins", True , 5),
    EnvironmentTemplate("Derelict Ruins", True, 4),
]

def set_environment() -> EnvironmentResult:
    chosen = random.choices(
        ENVIRONMENTS,
        weights=[env.chance for env in ENVIRONMENTS],
        k=1
    )[0]

    if chosen.is_ruin:
       ruin_type = pick_random(RUIN_TYPES, 1)
    else:
        ruin_type = None

    return EnvironmentResult(
        name=chosen.name,
        is_ruin=chosen.is_ruin,
        ruin_type=ruin_type,
    )