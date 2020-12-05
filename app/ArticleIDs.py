from app import app
from app.decorators import string
from flask import request, jsonify
from app.dbConnector import getArticlesIDs, updateArticleName, addArticleID, delArticleID

linksArticleIDs = {
    'getArticleIDs' : '/ids/getArticleIDs',
    'renameArticle' : '/renameArticle'
}


def initArticleIdsRoutes(self):
    @app.route( linksArticleIDs['getArticleIDs'], methods=['POST'])
    @string
    def getArticleIDs():
        return self.getIDs()

    @app.route( linksArticleIDs['renameArticle'], methods=['POST'])
    @string
    def renameArticle():
        data = request.get_json()
        print(data)
        return self.rename(data)     


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

    def rename(self, data):
        return updateArticleName(data['id'], data['name'])