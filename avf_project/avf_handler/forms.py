from django import forms
from .models import *

class ProductForm(forms.Form):
    article = forms.CharField(label='Артикул', max_length=100)
