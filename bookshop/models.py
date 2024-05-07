from django.db import models


class Author(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    year = models.DateField()

    class Meta:
        db_table = 'author'

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class BooksCategory(models.Model):
    categoryname = models.CharField(max_length=255)

    class Meta:
        db_table = 'BooksCategory'

    def __str__(self):
        return self.categoryname


class Books(models.Model):
    bookname = models.CharField(max_length=255)
    describtions = models.TextField()
    isbn = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='bookshop/', blank=True, null=True)
    year = models.DateField()
    book_category = models.ForeignKey(to=BooksCategory, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Books'

    def __str__(self):
        return self.bookname


class BooksAuthor(models.Model):
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'BooksAuthor'

    def __str__(self):
        return str(self.book)


class Review(models.Model):
    comment = models.TextField()
    stargiven = models.FloatField(default=1)
    user = models.CharField(max_length=255)
    book = models.ForeignKey(to=Books, on_delete=models.CASCADE)

    class Meta:
        db_table = 'review'

    def __str__(self):
        return self.user
