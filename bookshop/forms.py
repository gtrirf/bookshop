from django.forms import ModelForm
from .models import Books


class Bookform(ModelForm):
    class Meta:
        model = Books
        fields = '__all__'