from app import app
from app.decorators import string

from app.dbConnector import getArticlesIDs, updateArticleName, addArticleID, delArticleID

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
        initArticleIdsRoutes(self)

    def getIDs(self):
        return dict(getArticlesIDs())

    def deleteID(self, id):
        try:
            delArticleID(id)
        except Exception as e:
            print(31, e)            

    def addId(self, name: str, id: int):
        addArticleID(id, name)