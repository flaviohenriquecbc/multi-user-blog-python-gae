from handlers.handler import Handler
from models.user.user import User

class Signin(Handler):

    def get(self):
        self.render('signup/signin-form.html')

    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')

        u = User.login(username, password)
        if u:
            self.signin(u)
            self.redirect('/blog')
        else:
            msg = 'Invalid login'
            self.render('signup/signin-form.html', error = msg)
