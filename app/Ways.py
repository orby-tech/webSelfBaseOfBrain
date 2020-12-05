from app import app
from app.decorators import string
import json

from app.dbConnector import addWay, getWays, updateChildsWay, updateArticlesWay

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
            '0': {
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
        
        # import json
        # for i in self.ways:
        #     for j in [*i]:
        #         print(j)
        #         addWay(j, json.dumps(i[j]['childs']), json.dumps(i[j]['articles']))


        try:
            #loading articles from db
            pass
        except:
            pass

        initWaysRoutes(self)

    def getWays(self):
        ways = dict()
        for i in getWays():
            ways[str(i[0])] = { 
                'childs': json.loads(i[1]),
                'articles': json.loads(i[2])
            }
        return ways

    def deleteWay(self):
        pass

    def addWay(self, parentID: int, name: str, id: int):
        ways = dict()
        for i in getWays():
            ways[str(i[0])] = { 
                'childs': json.loads(i[1]),
                'articles': json.loads(i[2])
            }        
        ways[str(parentID)]['childs'].append(id)
        childs = json.dumps(ways[str(parentID)]['childs'])
        updateChildsWay(parentID, childs)
        addWay(id, json.dumps([]), json.dumps([]))

    def addArticles(self, parentID: int, id: int):
        ways = dict()
        for i in getWays():
            ways[str(i[0])] = { 
                'childs': json.loads(i[1]),
                'articles': json.loads(i[2])
            }        
        ways[str(parentID)]['articles'].append(id)
        articles = json.dumps(ways[str(parentID)]['articles'])
        updateArticlesWay(parentID, articles)
        addWay(id, json.dumps([]), json.dumps([]))        


    def deleteArticles(self, id: int):
        ways = dict()
        for i in getWays():
            print(i[2])
            ways[str(i[0])] = { 
                'childs': json.loads(i[1]),
                'articles': [int(j) for j in json.loads( i[2])]
            }
        print(ways)        
        for i in ways:
            try:
                print(type(ways[i]['articles'][0]), list(ways[i]['articles']))
            except:
                pass
            print(int(id) in list(ways[i]['articles']), id, ways[i]['articles'])
            if int(id) in list(ways[i]['articles']):
                print(ways[i]['articles'])
                ways[i]['articles'].pop(
                    ways[i]['articles'].index(int(id))
                )
                articles = json.dumps(ways[i]['articles'])
                updateArticlesWay(i, articles)        
            