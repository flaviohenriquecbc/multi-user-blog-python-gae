from google.appengine.ext import db

def blog_key(name = 'default'):
    return db.Key.from_path('blog', name)
