class Post:
    def __init__(self, post_id, text):
        self.id = post_id
        self.text = text


class Comment(Post):
    def __init__(self, post_id, reply_to, text):
        super().__init__(post_id, text)
        self.text = text
        self.reply_to = reply_to


post = Post(post_id=3545100301, text='Именно он')
comment = Comment(post_id=14881488, reply_to=3545100301, text='А кто он-то')

