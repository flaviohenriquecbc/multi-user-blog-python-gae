from google.appengine.ext import db

class Like(db.Model):
    user_id = db.IntegerProperty(required=True)
    post_id = db.IntegerProperty(required=True)
    liked = db.BooleanProperty(default=False)
