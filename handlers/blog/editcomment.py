from google.appengine.ext import db
from handlers.handler import Handler
from models.blog.post import Post
from models.blog.like import Like
from models.blog.comment import Comment
from controllers.blog.commentcontroller import comment_key
from controllers.user.usercontroller import users_key

class EditComment(Handler):

    def get(self, comment_id):

        if self.read_secure_cookie('user_id') == '':
            self.redirect('/signin')
            return

        key = db.Key.from_path('Comment', int(comment_id), parent=comment_key())
        comment = db.get(key)

        if not comment:
            self.error(404)
            return

        self.render('blog/editcomment.html', content=comment.content)

    def post(self, comment_id):

        content = self.request.get('content')
        user_name = self.read_secure_cookie('user_name')

        if content:

            if user_name == '':
                self.redirect('/signin')
                return

            key = db.Key.from_path('Comment', int(comment_id), parent=comment_key())
            comment = db.get(key)

            if comment.user_name != user_name:
                error = "Permission denied: You cannot edit this comment"
                self.render("blog/editcomment.html", content=content, error=error)
                return

            if not comment:
                self.error(404)
                return

            comment.content = content
            comment.put()

            self.redirect('/blog/%s' % comment.post_id)

        else:
            error = "content, please"
            self.render("blog/editcomment.html", content=content, error=error)
