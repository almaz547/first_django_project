from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, ListView
from .models import ApartmentUser
from .forms import RegistrationForm
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail


# Create your views here.
class UserLoginView(LoginView):
    template_name = 'userapp/login.html'

class ConfirmationListView(ListView):
    template_name = 'userapp/confirmat.html'

    def get_queryset(self):
        return

    def get(self, request, *args, **kwargs):
        email = kwargs['email']
        user = ApartmentUser.objects.get(email=email)
        user.is_active = True
        user.save()
        return super().get(request, *args, **kwargs)

class UserRegistrationsView(CreateView):
    model = ApartmentUser
    form_class = RegistrationForm
    template_name = 'userapp/register.html'
    success_url = reverse_lazy('realtyapp:index')

    def form_valid(self, form):

        send_mail(
            'Подтверждение подписки',

            f'Приветствуем, {form.cleaned_data["username"]}!'
            f'Для подтверждения подписки, пройдите, пожалуйста, по ссылке:'
            f' "http://127.0.0.1:8000/user/confirmat/{form.cleaned_data["email"]}/',

            f' "http://127.0.0.1:8000/user/register/',
            [form.cleaned_data['email']],
            fail_silently=False,
        )
        obje = form.save(commit=False)
        return super().form_valid(form)




