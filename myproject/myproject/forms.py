from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product

class RegistrationForm(UserCreationForm):
    # Ваш код для форми реєстрації
    pass

class LoginForm(AuthenticationForm):
    # Ваш код для форми входу
    pass

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']
