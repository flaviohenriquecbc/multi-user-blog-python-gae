from google.appengine.ext import db
from handlers.blog.posthandler import PostHandler
from models.blog.post import Post
from controllers.blog.blogcontroller import blog_key

class EditPage(PostHandler):
    def get(self, post_id):

        if self.read_secure_cookie('user_id') == '':
            self.redirect('/signin')
            return

        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)

        if not post:
            self.error(404)
            return

        if post.created_by != self.read_secure_cookie('user_name'):
            error = "Permission denied: You cannot edit this post"
            self.render("blog/permalink.html", subject=subject, content=content, error=error)
            return

        tags = ','.join(post.tags)
        self.render('blog/editpost.html', subject=post.subject, content=post.content, tags = tags)

    def post(self, post_id):
        subject = self.request.get('subject')
        content = self.request.get('content')
        tags = self.request.get('tags')
        tags_list = None
        if tags:
            tags_list = tags.split(",")

        if subject and content and tags and tags_list and len(tags_list) > 0:
            key = db.Key.from_path('Post', int(post_id), parent=blog_key())
            post = db.get(key)

            if not post:
                self.error(404)
                return

            if post.created_by != self.read_secure_cookie('user_name'):
                error = "Permission denied: You cannot edit this post"
                self.render("blog/permalink.html", subject=subject, content=content, error=error)
                return

            post.subject = subject
            post.content = content
            post.tags = tags_list
            post.put()
            self.redirect('/')
        else:
            error = "subject and content, please"
            self.render("blog/editpost.html", subject=subject, content=content, error=error)
