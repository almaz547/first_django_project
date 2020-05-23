from django.core.management.base import BaseCommand
from realtyapp.models import Category, Apartment, Area_city, Images, Message_user, Metro, Material, Street


# def check_object_in_base(model, name):
#     if name:
#         name_base = model.objects.filter(name=name)
#         if not name_base:
#             name_base = model.objects.create(name=name)
#     else:
#         name_base = ''
#     return name_base

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Category.objects.create(name='rent')
        # Category.objects.create(name='sale')

        # area = Area_city.objects.create(name='Авиастроительный')
        # area = Area_city.objects.create(name='Вахитовский')
        # area = Area_city.objects.create(name='Кировский')
        # area = Area_city.objects.create(name='Московский')

        # Area_city.objects.all().delete()

        # area = Area_city.e.filter(name='Авиастроительный').delete()
        # area = Area_city.objects.filter(name='Авиастроительный')
        # print(area)
        #
        # areas = Area_city.objects.all()
        # for area in areas:
        #     print(area.name)
        #
        # area_city = 'Авиастроительный'
        # area_base = check_object_in_base(model=Area_city, name=area_city)
        # print(f'39  area_base  {area_base}')
        # if area_base:
        #     print(f'area_base  {area_base}')
        #     for el in area_base:
        #         print(f'area_base.name  {el.name}')
        #
        # areas = Area_city.objects.all()
        # for area in areas:
        #     print(area.name)

        # images = Images.objects.all()
        # for image in images:
        #     print(f'image.image  {image.image}')
        #     print(f'image.apartment  {image.apartment}')
        #     print(f'image.apartment.url_object  {image.apartment.url_object}')



        # apartment = Apartment.objects.first()
        # print(f'apartment  {apartment}')
        # images = Images.objects.filter(apartment=apartment)
        # # print(f'images  {images}')
        # for image in images:
        #     print(f'image.image  {image.image}')

        # apartment = Apartment.objects.all()
        #
        # for elem in apartment:
        #     # print(elem.category.all())
        #     for el in elem.category.all():
        #         print(el.name)
        # categorys = Apartment.objects.f
        # print(f'apartment.category  {apartment.category}')
        # messages = Message_user.objects.all()
        # # print(f'messages  {messages}')
        # for message in messages:
        #     print(f'message.name  {message.name}')
        #     print(f'message.message  {message.message}')
        #     print(f'message.email  {message.email}')
        #     print(f'message.create  {message.create}')
        #     print(f'message.telefone  {message.telefone}')
        # x = 1
        # category = Category.objects.get(name='rent')
        # apartments = Apartment.objects.filter(category=category)
        # for apartment in apartments:
        #     print(f'apartment.url_object  {apartment.url_object}')
        #     print(f'apartment.description  {apartment.description}')

        # metro_names = Metro.objects.all()
        # # print(f'metro_names  {metro_names}')
        # list_metro_names = []
        # for metro_name in metro_names:
        #     # print(metro_name)
        #     list_metro_names.append(metro_name.name)
        # print(f'list_metro_names  {list_metro_names}')

        # apartments = Apartment.objects.all()
        # for apartment in apartments:
        #
        #     print(f'apartment  {apartment}')
        #     print(f'apartment.user  {apartment.user}')
        #     print(f'apartment.creator  {apartment.creator}')

        images = Images.objects.all()
        print(f'images 1  {images}')




        # for apartment in apartments:
        #     print(f'apartment  {apartment}')

        # areas = Area_city.objects.all()
        # # print(f'streets  {streets}')
        # list_areas = []
        # for area in areas:
        #     list_areas.append(area.name)
        #     print(area)
        # print(list_areas)


        # material = Material.objects.all()
        # print(f'material  {material}')

# area_city = forms.CharField(label='Район', widget=forms.
    #                            TextInput(attrs={'class': 'form-control'}))
    # area_city = forms.ModelChoiceField(label='Район', queryset = Area_city.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}))

# class UpdateApartmentForm(forms.ModelForm):
#     street = forms.CharField(label='Улица', widget=forms.
#                              TextInput(attrs={'placeholder': 'street', 'class': 'form-control'}))
#     class Meta:
#         model = Apartment
#         exclude = ('metro_distance_number', 'year_public', 'month_public', 'day_public',
#                    'time_public', 'url_object', 'street')
#     # metro_name = forms.ChoiceField(label='Метро', required=False, choices=GEEKS_CHOICES_METRO,
#     #                                widget=forms.Select(attrs={'class': 'form-control'}))
#     metro_name = forms.ModelChoiceField(label='Метро', required=False, queryset=Metro.objects.all(),
#                                         widget=forms.Select(attrs={'class': 'form-control'}))
#     # metro_name = forms.CharField(label='Метро', required=False,
#     #                                widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     floor_number = forms.CharField(label='Этаж',
#                                    widget=forms.TextInput(attrs={'placeholder': 'этаж', 'class': 'form-control'}))
#     metro_distance = forms.CharField(label='Путь до метро', required=False,
#                                      widget=forms.TextInput(
#                                          attrs={'placeholder': 'в мин. пешком', 'class': 'form-control'}))
#     total_square = forms.CharField(label='Общая площадь',
#                                    widget=forms.TextInput(attrs={'placeholder': 'кв.м.', 'class': 'form-control'}))
#     living_square = forms.CharField(label='Жилая площадь', required=False,
#                                     widget=forms.TextInput(attrs={'placeholder': 'кв.м.', 'class': 'form-control'}))
#     floor_total = forms.CharField(label='Всего этажей', widget=forms.
#                                   TextInput(attrs={'placeholder': 'количество этажей', 'class': 'form-control'}))
#     count_room = forms.ModelChoiceField(label='Комнат', queryset=Room_count.objects.all(),
#                                  widget=forms.Select(attrs={'class': 'form-control'}))
#     material = forms.ModelChoiceField(label='Материал', queryset=Material.objects.all(), widget=forms.
#                                Select(attrs={'placeholder': 'материал строения', 'class': 'form-control'}))
#
#     balcony_type = forms.ModelChoiceField(label='Тип балкона', required=False, queryset=Balcony.objects.all(),
#                                    widget=forms.Select(attrs={'placeholder': 'Балкон, Лоджия, их количество',
#                                                                 'class': 'form-control'}))
#     is_home_appliances = forms.CharField(label='Техника', widget=forms.
#                                          TextInput(
#         attrs={'placeholder': 'С техникой, какая, без техники', 'class': 'form-control'}))
#     is_furniture = forms.CharField(label='Мебель', widget=forms.
#                                    TextInput(
#         attrs={'placeholder': 'С мебелью, какая, без мебели', 'class': 'form-control'}))
#     cost = forms.CharField(label='Стоимость', widget=forms.
#                            TextInput(attrs={'placeholder': 'в руб.', 'class': 'form-control'}))
#     currency = forms.ModelChoiceField(label='Валюта', initial='руб', queryset=Currency.objects.all(),
#                                       widget=forms.Select(attrs={'class': 'form-control'}))
#     house_number = forms.CharField(label='Дом', widget=forms.
#                                    TextInput(attrs={'placeholder': 'номер дома', 'class': 'form-control'}))
#
#     city = forms.ModelChoiceField(label='Населенный пункт', initial='Казань', queryset=Sity.objects.all(),widget=forms.
#                            Select(attrs={'class': 'form-control'}))
#     area_city = forms.ModelChoiceField(label='Район', required=False, queryset=Area_city.objects.all(),
#                                   widget=forms.Select(attrs={'class': 'form-control'}))
#     advertising_object = forms.CharField(label='Краткая реклама', required=False, widget=forms.
#                                          TextInput(attrs={'class': 'form-control'}))
#     description = forms.CharField(label='Описание объекта', widget=forms.
#                                   Textarea(attrs={'class': 'form-control'}))
#     category = forms.ChoiceField(label='Тип объявления', choices=GEEKS_CHOICES_CATEGORY,
#                                  widget=forms.Select(attrs={'class': 'form-control'}))
#     # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Тип объявления', widget=forms.
#     #                                           CheckboxSelectMultiple())
#     сreator = forms.CharField(label='Создатель', initial='user',
#                               widget=forms.TextInput(attrs={'class': 'form-control'}))
#
#     # def clean_street(self):
#     #     street_name = self.cleaned_data['street']
#     #     print(f'street_name  {street_name}')
#     #     return street_name

# https://github.com/almaz547/first_django_project/pull/2