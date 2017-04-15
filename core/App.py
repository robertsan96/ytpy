import sys

from core.RunType import *
from core.types.QuickType import QuickType
from core.types.ManualType import ManualType

class App:

    runType = None

    def __init__(self):
        self.runType = getRunType()
        self.runApp(self.runType)

    def runApp(self, runType):
        if runType == RunType.MANUAL:
            runApp = ManualType()
        else:
            runApp = QuickType(sys.argv[1])
