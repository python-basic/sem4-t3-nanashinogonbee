class Guestbook():
    def __init__(self, *, first_name, last_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def show_info(self):
        return 'Имя: {}\nФамилия: {}\nТелефон: {}'.format(
            self.first_name,
            self.last_name,
            self.phone
            )

guestbook = Guestbook(first_name='Иван', last_name='Иванов', phone='+12345678')
print(guestbook.show_info())

