from google.appengine.ext import db
from handlers.blog.posthandler import PostHandler
from models.blog.post import Post
from controllers.blog.blogcontroller import blog_key

class DeletePage(PostHandler):
    def post(self, post_id):

        if self.read_secure_cookie('user_id') == '':
            self.redirect('/signin')
            return

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        if post.created_by != self.read_secure_cookie('user_name'):
            error = "Permission denied: You cannot delete this post"
            self.render("blog/permalink.html", subject=subject, content=content, error=error)

        post.delete()

        self.redirect('/')
