from google.appengine.ext import db
from handlers.blog.posthandler import PostHandler
from models.blog.post import Post
from models.blog.like import Like
from controllers.blog.blogcontroller import blog_key

class PostPage(PostHandler):
    def get(self, post_id):
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        user_id = self.read_secure_cookie('user_id')

        if user_id:

            like = Like.all().filter('user_id =',
                        int(user_id)).filter('post_id = ', int(post.key().id())).get()

            if like and like.liked:
                post.you_liked = True

        if not post:
            self.error(404)
            return

        self.render('blog/permalink.html', post = self.render_post(post))
