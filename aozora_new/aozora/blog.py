from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db
from . import image_get
import itertools
from pprint import pprint


bp = Blueprint('blog', __name__)


@bp.route('/<idw>')
def indexblog(idw):
    """Show all the posts, most recent first."""
    db = get_db()
    if len(idw)==6:
        posts = db.execute(
            'SELECT * FROM aosora WHERE FIGUREID = ?',
            #   'SELECT p.id, title, body, created, author_id, username'
            #   ' FROM post p JOIN user u ON p.author_id = u.id'
            # ' ORDER BY created DESC'
            (idw,)
        ).fetchall()
        images = image_get.image_get(posts[0]['WRITERNAME'], len(posts))

        posts2 = []
        if len(posts) >= len(images):
            for i, a in zip(posts, range(len(images))):
                # pprint.pprint(i['WRITERNAME'])
                posttem = dict()
                posttem['WRITERNAME'] = i['WRITERNAME']
                posttem['ORGINNAME'] = i['ORGINNAME']
                posttem['WORKNAME'] = i['WORKNAME']
                posttem['url'] = ' <img class="activator" src="' + images[a] + '">'
                posts2.append(posttem)

            for i in posts[5:]:
                # pprint.pprint(i['WRITERNAME'])
                posttem = dict()
                posttem['WRITERNAME'] = i['WRITERNAME']
                posttem['ORGINNAME'] = i['ORGINNAME']
                posttem['WORKNAME'] = i['WORKNAME']
                posttem['url'] = ' 画像が足りない。。。'
                posts2.append(posttem)
        else:
            for i, a in zip(posts, range(len(images))):
                # pprint.pprint(i['WRITERNAME'])
                posttem = dict()
                posttem['WRITERNAME'] = i['WRITERNAME']
                posttem['ORGINNAME'] = i['ORGINNAME']
                posttem['WORKNAME'] = i['WORKNAME']
                posttem['url'] = ' <img class="activator" src="' + images[a] + '">'
                posts2.append(posttem)
    else:
        posts2=[]
        # print(type(idw))
        # print(type(str(idw)))
        # print(type(len(str(idw))))
        # print(len(str(idw))/6)
        # print(type(len(str(idw))/6))

        for i in range(int(len(str(idw))/6)):

            keyid=idw[i*6:i*6+6]
            print(keyid)
            db = get_db()

            posts = db.execute(
               'SELECT * FROM aosora WHERE FIGUREID = ?',
                #   'SELECT p.id, title, body, created, author_id, username'
                #   ' FROM post p JOIN user u ON p.author_id = u.id'
                # ' ORDER BY created DESC'
                (keyid,)
            ).fetchall()

            images = image_get.image_get(posts[0]['WRITERNAME'], len(posts))
            print(len(images))
            print(type(len(images)))
            if len(posts) >= len(images):
                for i, a in zip(posts, range(len(images))):
                    # pprint.pprint(i['WRITERNAME'])
                    posttem = dict()
                    posttem['WRITERNAME'] = i['WRITERNAME']
                    posttem['ORGINNAME'] = i['ORGINNAME']
                    posttem['WORKNAME'] = i['WORKNAME']
                    posttem['url'] = ' <img class="activator" src="' + images[a] + '">'
                    posts2.append(posttem)

                for i in posts[len(images):]:
                    # pprint.pprint(i['WRITERNAME'])
                    posttem = dict()
                    posttem['WRITERNAME'] = i['WRITERNAME']
                    posttem['ORGINNAME'] = i['ORGINNAME']
                    posttem['WORKNAME'] = i['WORKNAME']
                    posttem['url'] = ' 画像が足りない。。。'
                    posts2.append(posttem)
            else:
                for i, a in zip(posts, range(len(images))):
                    # pprint.pprint(i['WRITERNAME'])
                    posttem = dict()
                    posttem['WRITERNAME'] = i['WRITERNAME']
                    posttem['ORGINNAME'] = i['ORGINNAME']
                    posttem['WORKNAME'] = i['WORKNAME']
                    posttem['url'] = ' <img class="activator" src="' + images[a] + '">'
                    posts2.append(posttem)

    print(posts[0]['WRITERNAME'],len(posts))
    aa=posts[0]['WRITERNAME'][0]
    print(aa)
    images=image_get.image_get(posts[0]['WRITERNAME'],len(posts))
    pprint(images)
    # posts=dict(posts)
    #
    # desc = posts.description
    # column_names = [col[0] for col in desc]
    # posts = [dict(itertools.izip(column_names, row))
    #         for row in posts.fetchall()



    posts = posts2

    tail=divmod(len(posts),6)
    postslst=[[],[],[],[],[],[]]
    if tail[0]==0:
        print(tail)
        for tem,t in zip(posts,range(tail[1])):
            postslst[t].append(tem)
    else:
        for t in range(tail[0]):
            postslst[0].append(posts[6*t])
            postslst[1].append(posts[6*t+1])
            postslst[2].append(posts[6*t+2])
            postslst[3].append(posts[6*t+3])
            postslst[4].append(posts[6*t+4])
            postslst[5].append(posts[6*t+5])
        for t in range(tail[1]):
            postslst[t].append(posts[6*tail[0]+t])
    # pprint(postslst)

    return render_template('blog/indexblog.html', postslst0=postslst[0],postslst1=postslst[1],postslst2=postslst[2],postslst3=postslst[3],postslst4=postslst[4],postslst5=postslst[5])


def get_post(writer_name, check_author=True):
    """Get a post and its author by writer_name.

    Checks that the id exists and optionally that the current user is
    the author.

    :param id: id of post to get
    :param check_author: require the current user to be the author
    :return: the post with author information
    :raise 404: if a post with the given id doesn't exist
    :raise 403: if the current user isn't the author
    """
    post = get_db().execute(
        # 'SELECT p.id, title, body, created, author_id, username'
        # ' FROM post p JOIN user u ON p.author_id = u.id'
        # ' WHERE p.id = ?',
        'SELECT * FROM aosora WHERE WRITERNAME = ?',
        # 'SELECT p.id, title, body, created, author_id, username'
        # ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY WORKID DESC'
        (writer_name, )

        # (id,)
    ).fetchall()

    if post is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    """Create a new post for the current user."""
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    """Update a post if the current user is the author."""
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ? WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    """Delete a post.

    Ensures that the post exists and that the logged in user is the
    author of the post.
    """
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
