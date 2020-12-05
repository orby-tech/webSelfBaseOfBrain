from app import app
from app.decorators import string

from app.dbConnector import addWaysID, getWaysIDs, updateWaysName, deleteWaysID

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
        initWaysIdsRoutes(self)

    def getIDs(self):
        return dict(getWaysIDs())

    def deleteId(self, id: int):
        return deleteWaysID(id)

    def addId(self, name: str, id: int):
        addWaysID(id, name)