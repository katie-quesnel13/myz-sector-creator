from dataclasses import dataclass, field
from typing import List, Any, Optional
from utitlityFunctions import *

@dataclass
class ThreatType:
    name: str
    chance: int

@dataclass
class Threat:
    name: str
    chance: int

THREAT_TYPES = [
    ThreatType("Humanoid", 2),
    ThreatType("Monster", 3),
    ThreatType("Phenomenon", 1),
]

HUMANOID_THREATS = [
    Threat("Amnesiac", 1),
    Threat("Beast Mutants", 2),
    Threat("Cannibals", 3),
    Threat("Doom Cultists", 2),
    Threat("Exiled Mutants", 3),
    Threat("Expedition from Another Ark", 3),
    Threat("Helldrivers", 3),
    Threat("Morlocks", 3),
    Threat("Nova Cultists", 2),
    Threat("Patrol from the Ark", 2),
    Threat("Scrap Oracle", 2),
    Threat("Wanderers", 2),
    Threat("Water Trader", 2),
    Threat("Wreckers", 2),
    Threat("Zone-Ghouls", 4)
]

MONSTER_THREATS = [
    Threat("Acid Grass", 2),
    Threat("Air Jellies", 1),
    Threat("Automaton", 1),
    Threat("Bitterbeasts", 2),
    Threat("Deathworm", 2),
    Threat("Devourer", 2),
    Threat("Grazers", 2),
    Threat("Gutfish (infected water)", 1),
    Threat("Killer Tree", 1),
    Threat("Mind Mosquitoes", 1),
    Threat("Nightmare Flowers", 1),
    Threat("Parasite Fungus", 1),
    Threat("Razorback", 1),
    Threat("Rot Ants", 2),
    Threat("Rotfish", 1),
    Threat("Scrap Crows", 2),
    Threat("Trash Hawk", 1),
    Threat("Worm Swarm", 1),
    Threat("Zone Dogs", 3),
    Threat("Zone Leeches", 2),
    Threat("Zone Rats", 3),
    Threat("Zone Spider", 2),
    Threat("Zone Wasps", 2)
]

PHENOMENON_THREATS = [
    Threat("Acid Rain", 3),
    Threat("Ash Storm", 2),
    Threat("Dust Tornado", 2),
    Threat("Electric Storm", 2),
    Threat("Ghost Lights", 1),
    Threat("Inertia Field", 1),
    Threat("Magnetic Field", 2),
    Threat("Mirage", 1),
    Threat("Mud Puddles", 2),
    Threat("Night Lights", 2),
    Threat("Obelisk", 1),
    Threat("Pillars of Light", 2),
    Threat("Rot Hotspot", 3),
    Threat("Rot Wind", 2),
    Threat("Sinkhole", 2),
    Threat("Temperature Drop / Heat Wave", 2),
    Threat("Unexploded Ordnance", 2),
    Threat("Vacuum", 1),
    Threat("Zone Smog", 3)
]

def roll_threat_code():
    code = [roll_d6(),  roll_d6(),  roll_d6(),  roll_d6(), roll_d6(),  roll_d6(),  roll_d6(), roll_d6(), roll_d6()]
    return code

def build_threat(code):
    threats = [None] * 9
    for n in range(9):
        if code[n] == 1:
            threat_type = random.choices(
                    THREAT_TYPES,
                    weights=[t.chance for t in THREAT_TYPES],
                    k=1
                )[0].name
            if threat_type == "Humanoid":
                threats[n] = random.choices(
                    HUMANOID_THREATS,
                    weights=[t.chance for t in HUMANOID_THREATS],
                    k=1
                )[0].name
            elif threat_type == "Monster":
                threats[n] = random.choices(
                    MONSTER_THREATS,
                    weights=[t.chance for t in MONSTER_THREATS],
                    k=1
                )[0].name
            elif threat_type == "Phenomenon":
                threats[n] = random.choices(
                    PHENOMENON_THREATS,
                    weights=[t.chance for t in PHENOMENON_THREATS],
                    k=1
                )[0].name
        elif code[n] == 6:
            threats[n] = "Artifact"
        else:
            threats[n] = None
    return threats