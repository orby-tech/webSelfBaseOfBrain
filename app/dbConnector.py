import sqlite3


# db to Articles

def addArticle(id: int, text: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''insert into articles values(?, ?)''', (int(id), str(text)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def updateArticle(id: int, text: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''update articles set id=?, text=? where id=?''', (int(id), str(text), int(id)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def getArticle(id: int):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        print(id)
        cursor.execute('''select * from articles where id=?''', (int(id),))
        answer = cursor.fetchall()
        con.close()
        return answer
    except Exception:
        return 'error'


# db ArticlesIDs
def addArticleID(id: int, name: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''insert into articlesIDs values(?, ?)''', (int(id), str(name)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def updateArticleName(id: int, name: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''update articlesIDs set id=?, name=? where id=?''', (int(id), str(name), int(id)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def getArticlesIDs():
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        print(id)
        cursor.execute('''select * from articlesIDs''')
        answer = cursor.fetchall()
        con.close()
        return answer
    except Exception:
        return 'error'

# db WaysIDs
def addWaysID(id: int, name: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''insert into waysIDs values(?, ?)''', (int(id), str(name)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def updateWaysName(id: int, name: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''update waysIDs set id=?, name=? where id=?''', (int(id), str(name), int(id)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def getWaysIDs():
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        print(id)
        cursor.execute('''select * from waysIDs''')
        answer = cursor.fetchall()
        con.close()
        return answer
    except Exception:
        return 'error'



# cursor.execute('''delete * from articles''')