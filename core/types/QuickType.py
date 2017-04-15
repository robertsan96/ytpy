from core.AppConfig import AppConfig

class QuickType:

    appConfig = AppConfig()

    def __init__(self, url):
        print "getting data from " + url + "and writing to " + self.appConfig.writePath
