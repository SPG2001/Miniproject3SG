# INF601 - Advanced Programming in Python
# Stephen Gabel
# Mini Project 3


from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskwiz.auth import login_required
from flaskwiz.db import get_db

bp = Blueprint('enemyposter', __name__)

#This is where the information is pulled from the database for posts to show on index.html

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, enemy_name, enemy_health, enemy_resistance, enemy_rank, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('enemyposter/index.html', posts=posts)

#When a user creates a post, this is what runs. It updates the database with the information the post contains.

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        enemy_name = request.form['enemy_name']
        enemy_health = request.form['enemy_health']
        enemy_resistance = request.form['enemy_resistance']
        enemy_rank = request.form['enemy_rank']
        error = None

        if not enemy_name:
            error = 'enemy_name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (enemy_name, enemy_health, enemy_resistance, enemy_rank, author_id)'
                ' VALUES (?, ?, ?, ?, ?)',
                (enemy_name, enemy_health, enemy_resistance, enemy_rank, g.user['id'])
            )
            db.commit()
            return redirect(url_for('enemyposter.index'))

    return render_template('enemyposter/create.html')

#This retrieves posts.

def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, enemy_name, enemy_health, enemy_resistance, enemy_rank, created, author_id, username'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

#This is where posts are retrieved by update.html, where then the user can update them with new data.

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        enemy_name = request.form['enemy_name']
        enemy_health = request.form['enemy_health']
        enemy_resistance = request.form['enemy_resistance']
        enemy_rank = request.form['enemy_rank']
        error = None

        if not enemy_name:
            error = 'enemy_name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET enemy_name = ?, enemy_health = ?, enemy_resistance = ?, enemy_rank = ?,'
                ' WHERE id = ?',
                (enemy_name, enemy_health, enemy_resistance, enemy_rank, id)
            )
            db.commit()
            return redirect(url_for('enemyposter.index'))

    return render_template('enemyposter/update.html', post=post)

#This allows a user to remove a post from the database.
@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('enemyposter.index'))