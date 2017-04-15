import sys

from enum import Enum

class RunType(Enum):
    QUICK = 1
    MANUAL = 2

def getRunType():
    if len(sys.argv) == 1:
        return RunType.MANUAL
    else:
        return RunType.QUICK
