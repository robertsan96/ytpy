import sys

from core.RunType import *
from core.types.QuickType import QuickType

class App:

    runType = None

    def __init__(self):
        self.runType = getRunType()
        self.runApp(self.runType)

    def runApp(self, runType):
        if runType == RunType.MANUAL:
            print "MANUAL"
        else:
            runApp = QuickType(sys.argv[1])
