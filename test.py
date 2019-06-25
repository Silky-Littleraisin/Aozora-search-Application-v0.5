
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
import sqlite3
import pprint

from image_get import image_get
import itertools

def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    db = sqlite3.connect(
            '/Users/silky/Documents/GitHub/aozora_new/instance/aosora.sqlite3',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
    db.row_factory = sqlite3.Row

    return db


db = get_db()
posts = db.execute(
    'SELECT * FROM aosora WHERE FIGUREID = ?',
    #   'SELECT p.id, title, body, created, author_id, username'
    #   ' FROM post p JOIN user u ON p.author_id = u.id'
    # ' ORDER BY created DESC'
    ('000148',)
).fetchall()
db.close()
images = image_get(posts[0]['WRITERNAME'], len(posts))
# posts=dict(posts)
#
# desc = posts.description
# column_names = [col[0] for col in desc]
# posts = [dict(itertools.izip(column_names, row))
#         for row in posts.fetchall()

posts2 = []
for i, a in zip(posts, range(len(images))):
    pprint.pprint(i['WRITERNAME'])
    posttem = dict()
    posttem['WRITERNAME']=i['WRITERNAME']
    posttem['ORGINNAME']=i['ORGINNAME']
    posttem['WORKNAME']=i['WORKNAME']
    posttem['url'] = images[a]
    posts2.append(posttem)

posts=posts2
print(posts2)
tail = divmod(len(posts), 6)
postslst = [[], [], [], [], [], []]
if tail[0] == 0:
    for tem, t in zip(posts, range(tail[1])):
        postslst[t] = tem
else:
    for t in range(tail[0]):
        postslst[0].append(posts[6 * t])
        postslst[1].append(posts[6 * t + 1])
        postslst[2].append(posts[6 * t + 2])
        postslst[3].append(posts[6 * t + 3])
        postslst[4].append(posts[6 * t + 4])
        postslst[5].append(posts[6 * t + 5])
    for t in range(tail[1]):
        postslst[t].append(posts[6 * tail[0] + t])

