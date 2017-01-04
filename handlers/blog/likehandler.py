from google.appengine.ext import db
from handlers.handler import Handler
from models.blog.post import Post
from models.blog.like import Like
from controllers.blog.blogcontroller import blog_key
from controllers.user.usercontroller import users_key

class LikeHandler(Handler):

    def post(self, post_id):

        user_id = self.read_secure_cookie('user_id')
        if user_id == '':
            self.redirect('/signin')
            return

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if self.read_secure_cookie('user_id') == post.created_by:
            self.redirect('/')
            return

        like = Like.all().filter('user_id =', int(user_id)).filter('post_id = ', int(post_id)).get()

        if like:
            if like.liked:
                post.nr_likes = post.nr_likes - 1
            else:
                post.nr_likes = post.nr_likes + 1

            like.liked = not like.liked
        else:
            like = Like(user_id=int(user_id), post_id=int(post_id), liked=True)
            post.nr_likes = post.nr_likes + 1

        like.put()
        post.put()

        self.redirect('/blog/%s' % str(post_id))
