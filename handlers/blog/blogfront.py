from handlers.blog.posthandler import PostHandler
from models.blog.post import Post
from models.blog.like import Like

class BlogFront(PostHandler):
    def get(self):
        posts = Post.all().order('-created')

        user_id = self.read_secure_cookie('user_id')

        posts_array = []
        if user_id:
            for post in posts:
                like = Like.all().filter('user_id =', int(user_id)).filter('post_id = ', int(post.key().id())).get()
                if like and like.liked:
                    post.you_liked = True
                posts_array.append(post)
        else:
            posts_array = posts

        # posts = db.GqlQuery("select * from Post order by created desc limit 10")
        self.render('blog/front.html', posts = self.render_posts(posts_array))
