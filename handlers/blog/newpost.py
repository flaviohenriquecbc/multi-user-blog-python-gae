from google.appengine.ext import db
from handlers.handler import Handler
from models.blog.post import Post
from controllers.blog.blogcontroller import blog_key

class NewPost(Handler):
    def get(self):
        if self.read_secure_cookie('user_id') == '':
            self.redirect('/signin')
            return

        self.render("blog/newpost.html")

    def post(self):
        subject = self.request.get('subject')
        content = self.request.get('content')
        tags = self.request.get('tags')
        tags_list = None
        if tags:
            tags_list = tags.split(",")
        created_by = self.read_secure_cookie('user_name')

        if subject and content and tags and tags_list and len(tags_list) > 0:
            p = Post(parent = blog_key(), subject = subject, content = content, created_by = created_by, tags = tags_list)
            p.put()
            self.redirect('%s' % str(p.key().id()))
        else:
            error = "subject and content, please"
            self.render("blog/newpost.html", subject=subject, content=content, error=error)
