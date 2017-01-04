from handlers.handler import Handler
from models.user.user import User
from controllers.user.usercontroller import *
from handlers.user.signin import Signin

class Signup(Handler):

    def get(self):
        self.render("signup/index.html", params=None, valid=None)

    def post(self):
        self.username = self.request.get("username")
        self.password = self.request.get("password")
        self.verify = self.request.get("verify")
        self.email = self.request.get("email")
        params = {
                    "username": self.username,
                    "password": self.password,
                    "verify": self.verify,
                    "email": self.email
                }

        valid = {
                    "username": valid_username(self.username) != None,
                    "password": (valid_password(self.password) != None) and self.password == self.verify,
                    "email": self.email == "" or (valid_email(self.email) != None)
                }

        if valid["username"] and valid["password"] and valid["email"]:
            self.done()
        else:
            self.render("signup/index.html", params=params, valid=valid)

    def done(self, *a, **kw):
        raise NotImplementedError

class Register(Signup):
    def done(self):
        #make sure the user doesn't already exist
        u = User.by_name(self.username)
        if u:
            msg = 'That user already exists.'
            self.render('signup/signup-form.html', error_username = msg)
        else:
            u = User.register(self.username, self.password, self.email)
            u.put()

            self.signin(u)
            self.redirect('/blog')
