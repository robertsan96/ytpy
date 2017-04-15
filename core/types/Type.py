import sys
import requests
import fileinput

from core.AppConfig import AppConfig
from core.parser.Parser import Parser
from core.models.Video import Video
from glob import glob
from json import JSONEncoder

class Type:

    appConfig = AppConfig()
    parser = Parser()

    response = None
    video = Video()

    def getSource(self, url):
        try:
            response = requests.get(url)
            if response.status_code != 200:
                raise Exception()
            self.response = response
        except Exception:
            print "Something went wrong with the request."
            sys.exit()
    
    def buildModel(self):
        self.video.url = self.response.url
        self.video.title = self.parser.getTitle(self.response.content)
        self.video.author = self.parser.getAuthor(self.response.content)
    
    def writeToFile(self):
        files = len(glob(self.appConfig.writePath + "*"))
        fileName = self.appConfig.fileNamePrefix + str(files + 1)
        extension = self.appConfig.fileNameExtension
        path = self.appConfig.writePath + fileName + extension
        
        newFile = open(path, "w")
        newFile.write(self.video.toJSON())
        newFile.close()
        print "Stored. [" + newFile.name + "]"
