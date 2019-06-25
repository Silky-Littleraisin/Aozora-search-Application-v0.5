import sqlite3

DATABASE ='/Users/silky/Documents/GitHub/aozora_new/instance/aosora.sqlite3'


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    db = sqlite3.connect(
           DATABASE,
           detect_types=sqlite3.PARSE_DECLTYPES
        )
    db.row_factory = sqlite3.Row

    return db


db = get_db()


with open('writer_name.txt','w') as file:
    for i in db.execute(
        'SELECT WRITERNAME FROM aosora'
    ).fetchall():

        file.write(i['WRITERNAME'])
        file.write('\n')


