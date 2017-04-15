import sys
import requests

from core.AppConfig import AppConfig
from core.parser.Parser import Parser
from core.models.Video import Video

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
        self.video.title = self.parser.getTitle(self.response.content)