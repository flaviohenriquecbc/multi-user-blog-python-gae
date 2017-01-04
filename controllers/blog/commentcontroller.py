from google.appengine.ext import db

def comment_key(name = 'default'):
    return db.Key.from_path('comment', name)
