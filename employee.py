import mysql.connector as sql
from texttable import Texttable

roomFields=["ROOM_NO", "CATEGORY", "ALLOTED_TO","RENT", "DATE_IN", "DATE_OUT"]
roomDtype=['t', 't', 't', 'i', 't', 't']
roomadd=["ROOM_NO", "CATEGORY", "RENT"]

def view(subj, fields, dtype):
    con=sql.connect(host='localhost', user='root', passwd='root', database='hotel_management')
    mycursor = con.cursor()
    mycursor.execute(f"SELECT * FROM {subj}")
    result = mycursor.fetchall()
    if result:
        result.insert(0,fields)
        t=Texttable(0)
        t.set_cols_dtype(dtype)
        t.add_rows(result)
        print(t.draw())
        return True
    else:
        print("NOTHING TO SEE HERE....")
        return False
    con.close()

view('rooms', roomFields, roomDtype)