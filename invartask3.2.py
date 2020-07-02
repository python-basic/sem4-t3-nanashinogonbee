import pendulum
import random
from pprint import pprint
import time

class Main:
    catalogue = []


class Post:
    schema = {
        'id': 0,
        'author': '',
        'text': '',
        'date': '',
        'comments': [],
        'private': None,
        'deleted': None,
        }


    def make(self, author, text, private=False):
        Post.text = text
        Post.schema['id'] = Post.schema['id'] + 1
        Post.schema['author'] = author
        Post.schema['text'] = Post.text
        Post.schema['date'] = pendulum.now()
        Post.schema['private'] = private
        Post.schema['deleted'] = False
        Main.catalogue.append(Post.schema)
        Post.schema = {
            'id': Post.schema['id'],
            'author': '',
            'text': '',
            'date': '',
            'comments': [],
            'private': None,
            'deleted': None,
            }


    def view(self, id):
        for post in Main.catalogue:
            if id in post.values():
                return post



class Comment:
    schema = {
        'comment_id': 0,
        'post_id': None,
        'author': '',
        'text': '',
        'date': '',
        'replies': [],
        }


    def make(self, post_id, author, text):
        Comment.schema['comment_id'] = Comment.schema['comment_id'] + 1
        Comment.schema['post_id'] = post_id
        Comment.schema['author'] = author
        Comment.schema['text'] = text
        Comment.schema['date'] = pendulum.now()

        for post in Main.catalogue:
            if post_id in post.values():
                post['comments'].append(Comment.schema)

        Comment.schema = {
            'comment_id': Comment.schema['comment_id'],
            'author': '',
            'text': '',
            'date': '',
            'comments': [],
            'private': None,
            'deleted': None,
            }


    def view(self, id):
        for post in Main.catalogue:
            if id in post.values():
                return post



post = Post()
comment = Comment()


post.make('user1', 'Hi!', private=False)
post.make('user2', 'damn what is this thing', private=True)

pprint(Main.catalogue)

print('\n\n')

pprint(post.view(id=2))

time.sleep(2)

comment.make(
    author='user1',
    post_id=2,
    text='This is a Facebook killer, didn\'t you know?'
    )

pprint(post.view(id=2))
