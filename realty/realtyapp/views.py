from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from realtyapp.models import Apartment, Category, Images, Message_user, Street, Images_url, Metro, Room_count
from realtyapp.models import Material, Balcony, Currency, Sity, Area_city
from .forms import MessageForm, ApartmentForm
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin


def check_object(model, name):
    objects_base = model.objects.all()
    for object_base in objects_base:
        if object_base.name == name:
            return object_base
    object_base = model.objects.create(name=name)
    return object_base

# def main_view(request):
#     return render(request, 'realtyapp/index.html', context={})

class IndexListView(ListView):
    template_name = 'realtyapp/index.html'

    def get_queryset(self):
        return

# def sale(request):
#     id_category = Category.objects.get(name='sale')
#     sales = Apartment.objects.filter(category=id_category)
#     return render(request, 'realtyapp/sale.html', context={'sales': sales})

class SaleListView(ListView):
    model = Apartment
    template_name = 'realtyapp/sale.html'
    context_object_name = 'sales'

    def get_queryset(self):
        sales = Apartment.objects.filter(category__name__in=['sale', 'Продажа'])
        return sales

# def rent(request):
#     id_category = Category.objects.get(name='rent')
#     rents = Apartment.objects.filter(category=id_category)
#     return render(request, 'realtyapp/rent.html', context={'rents': rents})

class RentListView(ListView):
    model = Apartment
    template_name = 'realtyapp/rent.html'
    context_object_name = 'rents'

    def get_queryset(self):
        rents = Apartment.objects.filter(category__name__in=['rent', 'Аренда'])
        return rents

class New_buildingsListView(ListView):
    template_name = 'realtyapp/new_buildings.html'

    def get_queryset(self):
        return


# def new_buildings(request):
#     return render(request, 'realtyapp/new_buildings.html', context={})

# def message(request):
#     if request.method == 'GET':
#         message = MessageForm()
#         return render(request, 'realtyapp/message.html', context={'message': message})
#     else:
#         message = MessageForm(request.POST)
#         if message.is_valid():
#             name = message['name'].value()
#             email = message['email'].value()
#             text_message = message['message'].value()
#             # print(f'name  {name}')
#             # print(f'email  {email}')
#             # print(f'text_message  {text_message}')
#             message.save()
#
#             send_mail(
#                 'Response letter',
#                 f'{name} Ваше письмо получено {text_message}',
#                 '',
#                 [email],
#                 fail_silently=True,
#             )
#             return HttpResponseRedirect(reverse('realtyapp:index'))
#         else:
#             return render(request, 'realtyapp/message.html', context={'message': message})

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message_user
    form_class = MessageForm
    success_url = reverse_lazy('realtyapp/index.html')
    template_name = 'realtyapp/message.html'

    def form_valid(self, form):
        # print(f'form  {form}')
        name = form['name'].value()
        email = form['email'].value()
        text_message = form['message'].value()
        # print(f'name  {name}')
        # print(f'email  {email}')
        # print(f'text_message  {text_message}')
        send_mail(
            'Response letter',
            f'{name} Ваше письмо получено {text_message}',
            '',
            [email],
            fail_silently=True,
        )
        return HttpResponseRedirect(reverse('realtyapp:index'))
# def apartment(request, id):
#     apartment = get_object_or_404(Apartment, id=id)
#     categorys = apartment.category.all()
#     for category in categorys:
#         name_category = category.name
#     images = Images.objects.filter(apartment=apartment)
#     return render(request, 'realtyapp/apartment.html', context={'apartment': apartment, 'images': images,
#                                                                 'name_category': name_category})

class ApartmentDetailView(DetailView):
    model = Apartment
    template_name = 'realtyapp/apartment.html'
    context_object_name = 'apartment'

    def get(self, request, *args, **kwargs):
        self.apartment_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        apartment = Apartment.objects.get(pk=self.apartment_id)
        self.images_url = Images_url.objects.filter(apartment=apartment)
        self.images = Images.objects.filter(apartment=apartment)
        print(f'self.images  {self.images}')
        categorys = apartment.category.all()
        self.list_name_category = []
        for category in categorys:
            self.list_name_category.append(category.name)
        return get_object_or_404(Apartment, pk=self.apartment_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['images_url'] = self.images_url
        context['categorys'] = self.list_name_category
        context['images'] = self.images
        return context


# def personal_area(request):
#     return render(request, 'realtyapp/personal_area.html', context={})

class PersonalListView(UserPassesTestMixin, ListView):
    model = Apartment
    success_url = reverse_lazy('realtyapp:index')
    template_name = 'realtyapp/personal_area.html'
    # context_object_name = 'ads_user'

    def test_func(self):
        return self.request.user

    def get_queryset(self):
        apartments_user = Apartment.objects.filter(user=self.request.user).all()
        # self.images = []
        # for apartment in apartments_user:
        #     images_apartment = Images.objects.filter(apartment=apartment)
        #     self.images.append(images_apartment)
        return apartments_user


    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     print(f'self.images  {self.images}')
    #     context['images'] = self.images
    #     return context

class ApartmentCreateFormView(LoginRequiredMixin, FormView):
    form_class = ApartmentForm
    success_url = reverse_lazy('realtyapp:pers_area')
    template_name = 'realtyapp/create_apart.html'

    def form_valid(self, form):
        # print()
        # print(f'dir(form)  {dir(form)}')
        # print()
        # print(f'form.data  {form.data}')
        # print()
        # print(f'form.files  {form.files["images"]}')
        # print()
        metro = check_object(Metro, form.data['metro_name'])
        count_room = check_object(model=Room_count, name=form.data['count_room'])
        material = check_object(model=Material, name=form.data['material'])
        balcony_type = check_object(model=Balcony, name=form.data['balcony_type'])
        currency = check_object(model=Currency, name=form.data['currency'])
        street = check_object(model=Street, name=form.data['street'])
        city = check_object(model=Sity, name=form.data['city'])
        area_city = check_object(model=Area_city, name=form.data['area_city'])
        user = self.request.user
        category = check_object(model=Category, name=form.data['category'])

        imag = form.files.get('images', None)



        apartment = Apartment.objects.create(metro_name=metro, floor_number=form.data['floor_number'],
                                             metro_distance=form.data['metro_distance'], total_square=form.data['total_square'],
                                             living_square=form.data['living_square'], floor_total=form.data['floor_total'],
                                             count_room=count_room, material=material,
                                             balcony_type=balcony_type, is_home_appliances=form.data['is_home_appliances'],
                                             is_furniture=form.data['is_furniture'], cost=form.data['cost'],
                                             currency=currency, house_number=form.data['house_number'],
                                             street=street, city=city, area_city=area_city,
                                             advertising_object=form.data['advertising_object'], description=form.data['description'],
                                             user=user)
        if imag:
            image = Images.objects.create(image=imag, apartment=apartment)
        apartment.category.add(category)
        apartment.save()
        return super().form_valid(form)



class ApartmentUpdataView(UserPassesTestMixin, FormView):
    form_class = ApartmentForm
    success_url = reverse_lazy('realtyapp:pers_area')
    template_name = 'realtyapp/updata_apart.html'

    def test_func(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        self.apartment_id = kwargs['pk']
        self.apartment = Apartment.objects.get(pk=self.apartment_id)
        return super().get(self, request, *args, **kwargs)

    def get_success_url(self):
        # print(f'get_success_url(self)  {super().get_success_url()}')
        self.success_url = f'/apartment/{self.apartment_id}/'
        # print(f'self.success_url  {self.success_url}')
        return self.success_url



    def get_initial(self):
        # print(f'self.kwargs  {self.kwargs}')
        self.initial['metro_name'] = self.apartment.metro_name
        self.initial['floor_number'] = self.apartment.floor_number
        self.initial['metro_distance'] = self.apartment.metro_distance
        self.initial['total_square'] = self.apartment.total_square
        self.initial['living_square'] = self.apartment.living_square
        self.initial['floor_total'] = self.apartment.floor_total
        self.initial['count_room'] = self.apartment.count_room
        self.initial['material'] = self.apartment.material
        self.initial['balcony_type'] = self.apartment.balcony_type
        self.initial['is_home_appliances'] = self.apartment.is_home_appliances
        self.initial['is_furniture'] = self.apartment.is_furniture
        self.initial['cost'] = self.apartment.cost
        self.initial['currency'] = self.apartment.currency
        self.initial['house_number'] = self.apartment.house_number
        self.initial['street'] = self.apartment.street
        self.initial['city'] = self.apartment.city
        self.initial['area_city'] = self.apartment.area_city
        self.initial['advertising_object'] = self.apartment.advertising_object
        self.initial['description'] = self.apartment.description

        list_category = []
        for category in self.apartment.category.all():
            list_category.append(category)
        self.initial['category'] = list_category
        return super().get_initial()

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        images = Images.objects.filter(apartment=self.apartment)
        context['images'] = images
        return context

    def form_valid(self, form):

        apartment = Apartment.objects.get(pk=self.apartment_id)

        apartment.metro_name = check_object(Metro, form.cleaned_data['metro_name'])
        apartment.floor_number = form.cleaned_data['floor_number']
        apartment.metro_distance = form.cleaned_data['metro_distance']
        apartment.total_square = form.cleaned_data['total_square']
        apartment.living_square = form.cleaned_data['living_square']
        apartment.floor_total = form.cleaned_data['floor_total']
        apartment.count_room = check_object(Room_count, form.cleaned_data['count_room'])
        apartment.material = check_object(Material, form.cleaned_data['material'])
        apartment.balcony_type = check_object(Balcony, form.cleaned_data['balcony_type'])
        apartment.is_home_appliances = form.cleaned_data['is_home_appliances']
        apartment.is_furniture = form.cleaned_data['is_furniture']
        apartment.cost = form.cleaned_data['cost']
        apartment.currency = check_object(Currency, form.cleaned_data['currency'])
        apartment.house_number = form.cleaned_data['house_number']
        apartment.street = check_object(Street, form.cleaned_data['street'])
        apartment.city = check_object(Sity, form.cleaned_data['city'])
        apartment.area_city = check_object(Area_city, form.cleaned_data['area_city'])
        apartment.advertising_object = form.cleaned_data['advertising_object']
        apartment.description = form.cleaned_data['description']
        apartment.save()


        categorys = Category.objects.all()
        categor = False
        for category in categorys:
            if category.name == form.cleaned_data['category']:
                apartment.category.clear()
                apartment.category.add(category)
                categor = True


        if not categor:
            apartment.category.clear()
            categor = Category.objects.create(name=form.cleaned_data['category'])
            apartment.category.add(categor)

        apartment.save()
        if form.cleaned_data["images"]:
            Images.objects.create(image=form.cleaned_data['images'], apartment=apartment)

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.apartment = Apartment.objects.get(pk=kwargs['pk'])
        self.apartment_id = kwargs['pk']
        return super().post(request, *args, **kwargs)





class  ApartmentDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'realtyapp/delete_confirm.html'
    model = Apartment
    success_url = reverse_lazy('realtyapp:pers_area')

    def test_func(self):
        return self.request.user


class  ImageDeleteView(UserPassesTestMixin, DeleteView):
    template_name = 'realtyapp/delete_image_confirm.html'
    model = Images
    success_url = reverse_lazy('realtyapp:pers_area')

    def test_func(self):
        return self.request.user
