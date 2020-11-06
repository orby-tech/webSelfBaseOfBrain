from app import app
from app.decorators import string
linksArticleIDs = {
    'getArticleIDs' : '/ids/getArticleIDs',

}




def initArticleIdsRoutes(self):
    @app.route( linksArticleIDs['getArticleIDs'], methods=['POST'])
    @string
    def getArticleIDs():
        return self.getIDs()

class ArticleIDs(object): 
    def __init__(self):
        super().__init__()

        self.ids = {
            '1': 'Первая',
            '2': 'Second'
        }

        try:
            #loading articles from db
            pass
        except:
            pass

        initArticleIdsRoutes(self)

    def getIDs(self):
        return self.ids

    def deleteId(self):
        pass

    def addId(self):
        pass