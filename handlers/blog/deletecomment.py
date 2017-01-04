from google.appengine.ext import db
from handlers.blog.posthandler import PostHandler
from models.blog.post import Post
from controllers.blog.blogcontroller import blog_key
from controllers.blog.commentcontroller import comment_key

class DeleteComment(PostHandler):
    def post(self, comment_id):

        if self.read_secure_cookie('user_id') == '':
            self.redirect('/signin')
            return

        key = db.Key.from_path('Comment', int(comment_id), parent=comment_key())
        comment = db.get(key)

        if not comment:
            self.error(404)
            return

        if comment.user_name != self.read_secure_cookie('user_name'):
            error = "Permission denied: You cannot delete this post"
            self.render("blog/editcomment.html", content=comment.content, error=error)

        comment.delete()

        key = db.Key.from_path('Post', int(comment.post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        post.nr_comments = post.nr_comments - 1
        post.put()

        self.redirect('/blog/%s' % comment.post_id)
