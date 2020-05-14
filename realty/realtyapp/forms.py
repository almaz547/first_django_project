from django import forms
from .models import Message_user

class MessageForm(forms.ModelForm):
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.TextInput(attrs={'placeholder': 'Message', 'class': 'form-control'}))
    telefone = forms.CharField(label='Телефон',
                               widget=forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Message_user
        fields = '__all__'