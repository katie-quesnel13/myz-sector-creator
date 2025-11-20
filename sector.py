import random
from environments import *
from rotLevel import *
from threats import *
from utitlityFunctions import *

env = set_environment()
print(env.name)
if env.is_ruin:
    print(env.ruin_type)
else:
    print("No artifacts")
print(set_rot_level().name)
code = roll_threat_code()
print(code)
print(build_threat(code))