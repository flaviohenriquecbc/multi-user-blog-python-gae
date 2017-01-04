from google.appengine.ext import db

class Comment(db.Model):
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)
    user_name = db.StringProperty(required=True)
    post_id = db.IntegerProperty(required=True)
