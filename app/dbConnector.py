import sqlite3




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



# cursor.execute('''delete * from articles''')