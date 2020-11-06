from app import app

@app.route('/hello', methods=['GET'])
def hello_world():
    return 'Hello, World!'



from app.Articles import Articles
from app.ArticleIDs import ArticleIDs
from app.WaysIds import WaysIds
from app.Ways import Ways
articles = Articles()
articlesIds = ArticleIDs()
waysIds = WaysIds()
ways = Ways()

