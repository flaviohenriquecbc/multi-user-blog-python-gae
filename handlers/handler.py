import webapp2
import os
import jinja2
import hmac

from models.user.user import User

secret = 'amiRTa06m0E72uZ70cr9A3x1Pz1QtS2S'

index = os.path.dirname(__file__).rfind('/')
root_path = os.path.dirname(__file__)[:index]
template_dir = os.path.join(root_path, 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

class Handler(webapp2.RequestHandler):

    def signin(self, user):
        self.set_secure_cookie('user_id', str(user.key().id()))
        self.set_secure_cookie('user_name', str(user.username))

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'user_id=; Path=/')
        self.response.headers.add_header('Set-Cookie', 'user_name=; Path=/')

    def make_secure_val(self, val):
        return '%s|%s' % (val, hmac.new(secret, val).hexdigest())

    def check_secure_val(self, secure_val):
        val = secure_val.split('|')[0]
        if secure_val == self.make_secure_val(val):
            return val

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params, userName = self.read_secure_cookie('user_name'))

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def set_secure_cookie(self, name, val):
        cookie_val = self.make_secure_val(val)
        self.response.headers.add_header(
            'Set-Cookie',
            '%s=%s; Path=/' % (name, cookie_val))

    def read_secure_cookie(self, name):
        cookie_val = self.request.cookies.get(name)
        return cookie_val and self.check_secure_val(cookie_val)

    def initialize(self, *a, **kw):
        webapp2.RequestHandler.initialize(self, *a, **kw)
        uid = self.read_secure_cookie('user_id')
        self.user = uid and User.by_id(int(uid))
