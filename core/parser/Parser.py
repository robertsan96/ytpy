import textwrap

from bs4 import BeautifulSoup

class Parser:
    
    def getTitle(self, content):
        soup = BeautifulSoup(content, "lxml")
        title = soup.find("span", {"id": "eow-title"})
        if title != None:
            title = textwrap.dedent(title.text)
            title = textwrap.wrap(title)
            return title[0]
        return ""

    def getAuthor(self, content):
        soup = BeautifulSoup(content, "lxml")
        userInfoNode = soup.find("div", {"class": "yt-user-info"})
        if userInfoNode == None:
            return ""
        for children in userInfoNode.findChildren():
            if children.name == "a":
                author = textwrap.dedent(children.text)
                author = textwrap.wrap(author)
                return author[0]
        return ""
