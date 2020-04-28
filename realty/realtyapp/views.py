from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from realtyapp.models import Apartment, Category, Images, Message_user, Street, Images_url, Metro, Room_count
from realtyapp.models import Material, Balcony, Currency, Sity, Area_city
from .forms import MessageForm, ApartmentForm, UpdateApartmentForm
from django.urls import reverse, reverse_lazy
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView, View
from django.views.generic.edit import CreateView

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
        category = Category.objects.get(name='sale')
        sales = Apartment.objects.filter(category=category)
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
        category = Category.objects.get(name='rent')
        rents = Apartment.objects.filter(category=category)
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

class MessageCreateView(CreateView):
    model = Message_user
    form_class = MessageForm
    success_url = reverse_lazy('realtyapp/index.html')
    template_name = 'realtyapp/message.html'

    def form_valid(self, form):
        print(f'form  {form}')
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
        categorys = apartment.category.all()
        self.list_name_category = []
        for category in categorys:
            self.list_name_category.append(category.name)
        return get_object_or_404(Apartment, pk=self.apartment_id)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['images_url'] = self.images_url
        context['categorys'] = self.list_name_category
        return context


# def personal_area(request):
#     return render(request, 'realtyapp/personal_area.html', context={})

class PersonalListView(ListView):
    model = Apartment
    success_url = reverse_lazy('realtyapp:index')
    template_name = 'realtyapp/personal_area.html'
    context_object_name = 'ads_user'

    def get_queryset(self):

        ads_user = Apartment.objects.filter(сreator='user').all()

        return ads_user

class ApartmentCreateFormView(FormView):
    form_class = ApartmentForm
    # fields = '__all__'
    # model = Apartment
    success_url = reverse_lazy('realtyapp:pers_area')
    template_name = 'realtyapp/create_apart.html'

    def form_valid(self, form):

        metro = check_object(Metro, form.data['metro_name'])
        count_room = check_object(model=Room_count, name=form.data['count_room'])
        material = check_object(model=Material, name=form.data['material'])
        balcony_type = check_object(model=Balcony, name=form.data['balcony_type'])
        currency = check_object(model=Currency, name=form.data['currency'])
        street = check_object(model=Street, name=form.data['street'])
        city = check_object(model=Sity, name=form.data['city'])
        area_city = check_object(model=Area_city, name=form.data['area_city'])
        category = check_object(model=Category, name=form.data['category'])

        apartment = Apartment.objects.create(metro_name=metro, floor_number=form.data['floor_number'],
                                             metro_distance=form.data['metro_distance'], total_square=form.data['total_square'],
                                             living_square=form.data['living_square'], floor_total=form.data['floor_total'],
                                             count_room=count_room, material=material,
                                             balcony_type=balcony_type, is_home_appliances=form.data['is_home_appliances'],
                                             is_furniture=form.data['is_furniture'], cost=form.data['cost'],
                                             currency=currency, house_number=form.data['house_number'],
                                             street=street, city=city, area_city=area_city,
                                             advertising_object=form.data['advertising_object'], description=form.data['description'],
                                             сreator=form.data['сreator'])
        apartment.category.add(category)
        apartment.save()
        return super().form_valid(form)

    # def get_queryset(self):
    #
    #     return rents

    # def form_valid(self, form):
    #     print(f'form.data  {form.data}')
    #     count_room = form['count_room']
    #     print(f'count_room  {count_room}')
    #     street = form['street'].value()
    #     print(f'street  {street}')
    #     Street.objects.create(name=street)
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     print(f'form_invalid.errors  {form.errors}')
    #     return super().form_invalid(form)
    #
    # def post(self, request, *args, **kwargs):
    #     post = request.POST
    #     # print(f'post  {post}')
    #     self.count_room = post['count_room']
    #     # print(f'count_room  {self.count_room}')
    #     self.material = post['material']
    #     self.street = post['street']
    #     self.city = post['city']
    #     return super().post(request, *args, **kwargs)


# class ApartmentUpdataView(UpdateView):
#     form_class = UpdateApartmentForm
#     # fields = '__all__'
#     model = Apartment
#     success_url = reverse_lazy('realtyapp:pers_area')
#     template_name = 'realtyapp/updata_apart.html'
#
#     def get(self, request, *args, **kwargs):
#         self.apartment_id = kwargs['pk']
#         print(f'self.apartment_id  {self.apartment_id}')
#         apartment = Apartment.objects.get(pk=self.apartment_id)
#         print(f'apartment  {apartment}')
#         self.metro_name = apartment.metro_name
#         # print(f'self.metro_name  {self.metro_name}')
#         self.marerial = apartment.material
#         print(f'apartment.material  {apartment.material}')
#         form = UpdateApartmentForm(instance=apartment)
#         return render(request, 'realtyapp/updata_apart.html', context={'form': form})

class ApartmentUpdataView(View):
    def get(self, request, pk):
        apartment = Apartment.objects.get(pk=pk)
        form = UpdateApartmentForm(instance=apartment)
        return render(request, 'realtyapp/updata_apart.html', context={'form': form})

    def post(self, request, pk):
        apartment = Apartment.objects.get(pk=pk)
        new_form = UpdateApartmentForm(request.POST, instance=apartment)

        if new_form.is_valid():
            new_apartment = new_form.save()
            return redirect(new_apartment)
        return render(request, 'realtyapp/updata_apart.html', context={'form': new_form})
    # def get_queryset(self):
    #     apartment = Apartment.objects.get(pk=self.apartment_id)
    #     print(f'apartment  {apartment}')
    #     # print(f'apartment.metro_name  {apartment.metro_distance}')
    #     return apartment

    # def get_object(self, queryset=None):
    #
    #     return get_object_or_404(Apartment, pk=self.apartment_id)
    #
    #
    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #
    #     context['metro_name'] = self.metro_name
    #     print(f'self.apartment.metro_name   {self.metro_name}')
    #     return context

class  ApartmentDeleteView(DeleteView):
    template_name = 'realtyapp/delete_confirm.html'
    model = Apartment
    success_url = reverse_lazy('realtyapp:pers_area')
