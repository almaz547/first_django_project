from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from realtyapp.models import Apartment, Category, Images
from .forms import MessageForm
from django.urls import reverse
from django.core.mail import send_mail

# Create your views here.
def main_view(request):
    return render(request, 'realtyapp/index.html', context={})

def sale(request):
    id_category = Category.objects.get(name='sale')
    sales = Apartment.objects.filter(category=id_category)
    return render(request, 'realtyapp/sale.html', context={'sales': sales})

def rent(request):
    id_category = Category.objects.get(name='rent')
    rents = Apartment.objects.filter(category=id_category)
    return render(request, 'realtyapp/rent.html', context={'rents': rents})

def new_buildings(request):

    return render(request, 'realtyapp/new_buildings.html', context={})

def message(request):
    if request.method == 'GET':
        message = MessageForm()
        return render(request, 'realtyapp/message.html', context={'message': message})
    else:
        message = MessageForm(request.POST)
        if message.is_valid():
            name = message['name'].value()
            email = message['email'].value()
            text_message = message['message'].value()
            # print(f'name  {name}')
            # print(f'email  {email}')
            # print(f'text_message  {text_message}')
            message.save()

            send_mail(
                'Response letter',
                f'{name} Ваше письмо получено {text_message}',
                '',
                [email],
                fail_silently=True,
            )
            return HttpResponseRedirect(reverse('realtyapp:index'))
        else:
            return render(request, 'realtyapp/message.html', context={'message': message})


def apartment(request, id):
    apartment = get_object_or_404(Apartment, id=id)
    categorys = apartment.category.all()
    for category in categorys:
        name_category = category.name
    images = Images.objects.filter(apartment=apartment)
    return render(request, 'realtyapp/apartment.html', context={'apartment': apartment, 'images': images,
                                                                'name_category': name_category})
