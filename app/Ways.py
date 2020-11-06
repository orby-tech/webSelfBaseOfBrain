from app import app
from app.decorators import string
linksWays = {
    'getWays' : '/ways/getWays',

}


def initWaysRoutes(self):
    @app.route( linksWays['getWays'], methods=['POST'])
    @string
    def getWays():
        return self.getWays()


class Ways(object): 
    def __init__(self):
        super().__init__()

        self.ways =  { 
            'root': {
                'childs': ['1', '2', '3'],
                'articles': [ '1', '2', '3', '4', '5', '6' ]
            },
             '1': {
                'childs': [],
                'articles': [ '1', '2', '3', '4', '5', '6' ]
            },
             '2': {
                'childs': ['1',],
                'articles': [ '1', '2', '3', '4', '5', '6' ]
            },
             '3': {
                'childs': ['1', '2', '4'],
                'articles': []
            },
            '4': {
                'childs': ['1', '2'],
                'articles': []
            }},
        

        try:
            #loading articles from db
            pass
        except:
            pass

        initWaysRoutes(self)

    def getWays(self):
        return self.ways

    def deleteWay(self):
        pass

    def addWay(self):
        pass