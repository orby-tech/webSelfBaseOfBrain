from app import app
from app.decorators import string
linksIDs = {
    'getWaysIds' : '/ids/getWaysIds',

}




def initWaysIdsRoutes(self):
    @app.route( linksIDs['getWaysIds'], methods=['POST'])
    @string
    def getWaysIds():
        return self.getIDs()

class WaysIds(object): 
    def __init__(self):
        super().__init__()

        self.ids = {
            'root' : 'Разделы',
            '1': '1',
        }

        try:
            #loading articles from db
            pass
        except:
            pass

        initWaysIdsRoutes(self)

    def getIDs(self):
        return self.ids

    def deleteId(self):
        pass

    def addId(self):
        pass