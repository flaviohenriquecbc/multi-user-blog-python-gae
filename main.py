#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from handlers.user.signin import Signin
from handlers.user.signup import Register
from handlers.user.logout import Logout
from handlers.blog.blogfront import BlogFront
from handlers.blog.postpage import PostPage
from handlers.blog.editpage import EditPage
from handlers.blog.deletepage import DeletePage
from handlers.blog.newpost import NewPost
from handlers.blog.likehandler import LikeHandler
from handlers.blog.commenthandler import CommentHandler
from handlers.blog.editcomment import EditComment
from handlers.blog.deletecomment import DeleteComment

# import re

app = webapp2.WSGIApplication([
    ('/', BlogFront),
    ('/signup', Register),
    ('/signin', Signin),
    ('/logout', Logout),
    ('/blog/?', BlogFront),
    ('/blog/([0-9]+)/edit', EditPage),
    ('/blog/([0-9]+)/delete', DeletePage),
    ('/blog/([0-9]+)/like', LikeHandler),
    ('/blog/([0-9]+)/comment/add', CommentHandler),
    ('/comment/([0-9]+)/edit', EditComment),
    ('/comment/([0-9]+)/delete', DeleteComment),
    ('/blog/([0-9]+)', PostPage),
    ('/blog/newpost', NewPost),
], debug=True)
