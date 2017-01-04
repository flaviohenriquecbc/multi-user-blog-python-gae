from google.appengine.ext import db
from handlers.handler import Handler
from models.blog.post import Post
from models.blog.like import Like
from models.blog.comment import Comment
from controllers.blog.commentcontroller import comment_key
from controllers.blog.blogcontroller import blog_key
from controllers.user.usercontroller import users_key

class CommentHandler(Handler):

    def post(self, post_id):

        content = self.request.get('content')
        user_name = self.read_secure_cookie('user_name')

        if user_name == '':
            self.redirect('/signin')
            return

        if content:
            p = Comment(content = content, post_id = int(post_id), user_name = user_name, parent=comment_key())
            p.put()

            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            post.nr_comments = post.nr_comments + 1

            post.put()

            self.redirect('/blog/%s' % post_id)
        else:
            error = "content, please"
            self.render("blog/permalink.html", content=content, error=error)
