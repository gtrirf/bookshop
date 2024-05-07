from django.contrib import admin
from .models import Author, BooksCategory, Books, BooksAuthor, Review
# Register your models here.


admin.site.register(Author)
admin.site.register(BooksCategory)
admin.site.register(Books)
admin.site.register(BooksAuthor)
admin.site.register(Review)

