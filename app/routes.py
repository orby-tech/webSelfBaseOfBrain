from app import app
from flask import request, jsonify

from random import randint

from app.Articles import Articles
from app.ArticleIDs import ArticleIDs
from app.WaysIds import WaysIds
from app.Ways import Ways

articles = Articles()
articlesIds = ArticleIDs()
waysIds = WaysIds()
ways = Ways()


@app.route( '/article/addArticle', methods=['POST'])
def addArticle():
    data = request.get_json()
    print(data)


@app.route( '/addWay', methods=['POST'])
def addWay():
    data = request.get_json()
    name = str(data['name'])
    parentId = int(data['id'])
    newId = randint(1000000000,9999999999)
    waysIds.addId(name, newId)
    ways.addWay(parentId, name, newId)
    return "good"