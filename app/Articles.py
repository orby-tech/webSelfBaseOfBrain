from app import app
from app.decorators import string
from flask import request, jsonify

linksArticles = {
    'getArticle' : '/article/getArticle',

}





def initArticlesRoutes(self):
    @app.route( linksArticles['getArticle'], methods=['POST'])
    @string
    def getArticle():
        data = request.get_json()
        print(request)
        id = data["id"]
        return self.getArticle(id)


class Articles(object): 
    def __init__(self):
        super().__init__()

        self.articles = {
            '1': '111',
            '2': '222',
            '333': '333'
        }

        try:
            #loading articles from db
            pass
        except:
            pass

        initArticlesRoutes(self)

    def getArticle(self, id):
        return self.articles[id]

    def deleteArticle(self):
        pass

    def addArticle(self):
        pass