from flask import render_template,request,redirect,url_for, abort, flash
from . import main
from flask_login import login_required,current_user
from .forms import PostsForm,CommentsForm,UpdateProfile,SubscribeForm
from ..models import Posts,Comments,User,Subscribe
from .. import photos, db
from datetime import datetime

@main.route('/')
# @login_required
def home():

    '''
    View root page function that returns the general news sources by category
    '''
    # message = "Hello World"
    title="Terabyte"
    posts = Posts.query.order_by('-id').all()
   
    

    message= 'Welcome to the Blog'
    # return "Hello, World"
    return render_template('home.html',title=title,message=message,posts=posts,user=current_user)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@main.route('/post/new',methods = ['GET','POST'])
@login_required
def new_post():
    '''
    View pitch function that returns the pitch page and data
    '''
    form = PostsForm()

    if form.validate_on_submit() and form.category.data != 'Select':
        body = form.body.data
        category = form.category.data
        title = form.title.data

        new_post = Posts(body=body,category=category,title=title,user_id=current_user.id)
        new_post.save_post()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('new_post.html', pitch_form = form)
@main.route("/pitch/<int:id>/update", methods=['GET', 'POST'])
@login_required
def update_post(id):
    post = Posts.query.get_or_404(id)
    if post.user != current_user:
        abort(403)
    form = PostsForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('.post',id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.body.data = post.body
    return render_template('new_post.html', title='Update Post',
                           pitch_form=form)

@main.route("/pitch/<int:id>/delete", methods=['POST'])
@login_required
def delete_post(id):
    post = Posts.query.get_or_404(id)
    if post.user != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))


@main.route("/pitch/comment/<int:id>/delete", methods=['POST'])
@login_required
def delete_comment(id):
    comment = Comments.query.get_or_404(id)

    db.session.delete(comment)
    db.session.commit()
    flash('Comment has been deleted!', 'success')
    return redirect(url_for('main.home'))

@main.route("/pitch/<int:id>/full")
def post(id):
    post = Posts.query.get_or_404(id)
    return render_template('post.html', title=post.title, post=post)


@main.route('/pitch/<int:id>',methods = ['GET', 'POST'])
@login_required
def comment(id):

    comments_form = CommentsForm()
    # pitch = Pitches.query.get(pitch_id)
    posts = Posts.query.filter_by(id=id).first()
    print(posts)
    if comments_form.validate_on_submit():
        comment = comments_form.comment.data

        new_comment = Comments(the_comment=comment,posts_id=posts.id, user_id = current_user.id)
        db.session.add(new_comment)
        db.session.commit()

    comments_list = Comments.query.filter_by(posts_id=id).order_by("-id")
    print(comments_list)

    return render_template('comments.html', comments_form=comments_form,comments_list=comments_list)

@main.route('/subscribe',methods=["GET","POST"])
def subscribe():
    form=SubscribeForm()

    if form.validate_on_submit():
        subscriber = Subscribe(name=form.name.data,email=form.email.data)
        db.session.add(subscriber)
        db.session.commit()
        flash('You have sucessfully subscribed to get notifications.')
        return redirect(url_for('main.home'))
        title = 'Subscribe'
    return render_template('subscribe.html',subscribe_form=form)

