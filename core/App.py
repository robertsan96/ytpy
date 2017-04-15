import sys

from core.RunType import RunType

class App:

    runType = None

    def __init__(self):
        self.runType = self.getRunType()
        
    def getRunType(self):
        if len(sys.argv) == 1:
            return RunType.MANUAL
        else:
            return RunType.QUICK
