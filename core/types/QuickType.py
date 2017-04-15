from core.types.Type import Type

class QuickType(object, Type):

    def __init__(self, url):
        super(QuickType, self).getSource(url)
        super(QuickType, self).buildModel()
        super(QuickType, self).writeToFile()
