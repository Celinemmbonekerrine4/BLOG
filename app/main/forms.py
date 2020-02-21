from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField,TextAreaField,SubmitField


class Blog(FlaskForm):
    title = StringField('Write your blog title',validators=[Required()])
    blog = TextAreaField('Type your best blog',validators=[required()])
    submit = SubmitField('Submit')



