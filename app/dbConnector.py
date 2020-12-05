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
        print(int(id), str(text))
        con.commit()    
        con.close()
    except Exception as e:
        print(e)
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

def delArticle(id: int):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''delete from articles where id=?''', (int(id),))
        con.commit()    
        con.close()
        return "good"
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

def delArticleID(id: int):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''delete from articlesIDs where id=?''', (int(id),))
        con.commit()    
        con.close()
        return "good"
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

def deleteWaysID(id: int):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''delete from waysIDs where id=?''', (int(id),))
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

# db WaysIDs
def addWay(id: int, childs: str, articles: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''insert into ways values(?, ?, ?)''', (int(id), str(childs), str(articles)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def deleteWay(id: int):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''delete from ways where id=?''', (int(id),))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def updateChildsWay(id: int, childs: str):
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''update ways set childs=? where id=?''', (str(childs), int(id)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def updateArticlesWay(id: int, articles: str):
    print(articles)
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        cursor.execute('''update ways set articles=? where id=?''', (str(articles), int(id)))
        con.commit()    
        con.close()
    except Exception:
        return 'error'
    return 'good'

def getWays():
    try:
        con = sqlite3.connect("./baseOfBrain/webEditor/app.db")
        cursor = con.cursor()
        print(id)
        cursor.execute('''select * from ways''')
        answer = cursor.fetchall()
        con.close()
        return answer
    except Exception:
        return 'error'

# cursor.execute('''delete * from articles''')