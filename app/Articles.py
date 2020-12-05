from app import app
from app.decorators import string
from flask import request, jsonify


from app.dbConnector import addArticle, getArticle, updateArticle, delArticle

linksArticles = {
    'getArticle' : '/article/getArticle',
    'updateArticle': '/article/updateArticle'

}

def initArticlesRoutes(self):
    @app.route( linksArticles['getArticle'], methods=['POST'])
    @string
    def getArticle():
        data = request.get_json()
        return self.getArticle(data["id"])

    @app.route( linksArticles['updateArticle'], methods=['POST'])
    @string
    def updateArticle():
        data = request.get_json()
        return self.updateArticle(data['id'], data['text'])


class Articles(object): 
    def __init__(self):
        super().__init__()
        initArticlesRoutes(self)

    def getArticle(self, id):
        try:
            return getArticle(id)[0][1]
        except:
            return ''

    def deleteArticle(self, id):
        try:
            delArticle(id)
        except Exception as e:
            print(43, e)

    def addArticle(self, id: int):
        addArticle(id, '')

    def updateArticle(self, id, text):
        return updateArticle(id, text)    