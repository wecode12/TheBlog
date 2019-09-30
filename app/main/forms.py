from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PostsForm(FlaskForm):
    category = SelectField('Blog Category',
                              choices=[('Select','Select Category'), ('Celebrity Gossip', 'Celebrity Gossip'), ('Fashion', 'Fashion'),
                                       ('Music', 'Music'), ('Food', 'Food'),('Sports', 'Sports'),
                                       ('Technology', 'Technology'),('Travel', 'Travel'),('Nature', 'Nature')                                       
                                       ], validators=[Required()])
    title = StringField('Blog Title',validators = [Required()])
    body = TextAreaField('Blog Content',validators = [Required()])
    submit = SubmitField('Post')
    
class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment on post',validators = [Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class SubscribeForm(FlaskForm):
    email = StringField("Email",validators = [Required()])
    name = StringField("Your Name",validators = [Required()])
    submit= SubmitField('Subscribe')


