import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from aozora.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


# @bp.before_app_request
# def load_logged_in_user():
#     """If a user id is stored in the session, load the user object from
#     the database into ``g.user``."""
#     user_id = session.get('user_id')
#
#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()
#

@bp.route('/register', methods=('GET', 'POST'))
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == 'POST':
        write_name = request.form['writer_name']
        work_name = request.form['work_name']
        orgin_name = request.form['orgin_name']

        db = get_db()
        error = None
        #
        # if not writename:
        #     error = 'write name is required.'
        # elif not workname:
        #     error = 'work name is required.'
        # elif db.execute(
        #     'SELECT id FROM user WHERE username = ?', (username,)
        # ).fetchone() is not None:
        #     error = 'User {0} is already registered.'.format(username)

        # if error is None:
        #     # the name is available, store it in the database and go to
        #     # the login page
        #     db.execute(
        #         'INSERT INTO user (username, password) VALUES (?, ?)',
        #         (username, generate_password_hash(password))
        #     )
        #     db.commit()
        #     return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/search', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':

        writername = request.form['singleInput']
        # fitler_lst = request.form['multipleInput']

        # work_name = request.form['work_name']
        # origin_name = request.form['origin_name']

#       username = request.form['username']
#        password = request.form['password']
        db = get_db()
#         error = None
        aosora = db.execute(
             "SELECT FIGUREID FROM aosora WHERE WRITERNAME LIKE ?",("%"+str(writername)+"%",)
         ).fetchall()


        # if user is None:
        #     error = 'Incorrect username.'
        # elif not check_password_hash(user['password'], password):
        #     error = 'Incorrect password.'
        error = None
        if aosora == None:
            error='nofinding'
        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            # session['writer_name'] = aosora['FIGUREID']
            #session['writer_name'] = writer_name
            if len(aosora)==1:
                print(aosora[0]['FIGUREID'])
                return redirect(url_for('blog.indexblog',idw=aosora[0]['FIGUREID']))
            else:
                prealst=set()
                for i in aosora:
                    prealst.add(i['FIGUREID'])
                    print(i['FIGUREID'])
                alst=str()
                for i in prealst:
                    alst=alst+str(i)

                return redirect(url_for('blog.indexblog',idw=alst))


        flash(error)

    return render_template('auth/index2.html')


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for('index'))
