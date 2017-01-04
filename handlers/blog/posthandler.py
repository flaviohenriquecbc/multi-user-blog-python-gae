from handlers.handler import Handler
from models.blog.comment import Comment
class PostHandler(Handler):

    def render_post(self, post):
        post._render_text = post.content.replace('\n', '<br>')
        comments = Comment.all().filter('post_id = ', int(post.key().id())).order('-created')
        return self.render_str("blog/post.html", p = post, detailed = True,
                                                comments = self.render_comments(comments))

    def render_comments(self, comments):
        result = []
        for comment in comments:
            comment._render_text = comment.content.replace('\n', '<br>')
            result.append(self.render_str("blog/comment.html", comment = comment))
        return result

    def render_posts(self, posts):
        result = []
        for post in posts:
            post._render_text = post.content.replace('\n', '<br>')
            result.append(self.render_str("blog/post.html", p = post))
        return result
