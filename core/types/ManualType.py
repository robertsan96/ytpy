import textwrap

from core.types.Type import Type 

class ManualType(object, Type):

    def __init__(self):
        super(ManualType, self).getSource(self.askForURL())
        self.buildModel()
        self.askForTitle()
        self.askForAuthor()
        self.writeToFile()

    def askForURL(self):
        return raw_input("URL: ")
    
    def askForTitle(self):
        title = raw_input("Title ["+ self.video.title +"]: ")
        title = textwrap.dedent(title)
        if len(title) != 0:
            self.video.title = title
        
    def askForAuthor(self):
        author = raw_input("Author ["+ self.video.author +"]: ")
        author = textwrap.dedent(author)
        if len(author) != 0:
            self.video.author = author