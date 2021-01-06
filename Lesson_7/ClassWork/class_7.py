class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.author}: {self.title}'

    def __len__(self):
        return self.pages


b = Book('War & Peace', 'Leo Tolstoi', 1652)
print(b)
print(len(b))
