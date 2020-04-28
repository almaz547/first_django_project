from django import forms
from .models import Message_user, Apartment, Category, Metro, Area_city, \
    Balcony, Room_count, Material, Sity, Currency

class MessageForm(forms.ModelForm):
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.TextInput(attrs={'placeholder': 'Message', 'class': 'form-control'}))
    telefone = forms.CharField(label='Телефон', required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Telefone', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Message_user
        fields = '__all__'


    # metro_name = forms.CharField(label='Метро', required=False,
    #                        widget=forms.TextInput(attrs={'placeholder': 'Станция', 'class': 'form-control'}))
    # metro_name = forms.ChoiceField(choices=['Козья слобода ', 'Площадь Тукая ', 'Яшьлек ',
    #                                 'Дубравная ', 'Проспект Победы ', 'Северный вокзал ', 'Суконная слобода ',
    #                                 'Аметьево ', 'Горки ', 'Авиастроительная '],
    #                        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))
    # metro_name =  forms.ModelChoiceField(queriset = Metro.objects.filter(name=['Козья слобода ', 'Площадь Тукая ', 'Яшьлек ',
    #                                 'Дубравная ', 'Проспект Победы ', 'Северный вокзал ', 'Суконная слобода ',
    #                                 'Аметьево ', 'Горки ', 'Авиастроительная ']))
    # metro_name =  forms.ModelChoiceField(label='Метро', required=False, queryset = Metro.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}))
    # metro_name = forms.ChoiceField(label='Метро', required=False, choices=[('Козья слобода',), ('Площадь Тукая ',), 'Яшьлек ',
    #                                 ('Дубравная',), ('Проспект Победы',), ('Северный вокзал',), ('Суконная слобода',),
    #                                  ('Аметьево',), ('Горки',), ('Авиастроительная',)])
GEEKS_CHOICES_METRO = (('', ''),
                 ('Площадь Тукая', 'Площадь Тукая'),
                 ('Дубравная', 'Дубравная'),
                 ('Проспект Победы', 'Проспект Победы'),
                 ('Северный вокзал', 'Северный вокзал'),
                 ('Суконная слобода', 'Суконная слобода'),
                 ('Аметьево', 'Аметьево'),
                 ('Горки', 'Горки'),
                 ('Авиастроительная', 'Авиастроительная'),
                  ('1Козья слобода', 'Козья слобода'),
                 ('Яшьлек', 'Яшьлек'),
                       ('Кремлёвская', 'Кремлёвская'))
GEEKS_CHOICES_AREA = (('', ''),
                      ('Кировский', 'Кировский'),
                      ('Вахитовский', 'Вахитовский'),
                      ('Ново-Савиновский', 'Ново-Савиновский'),
                      ('Московский', 'Московский'),
                      ('Приволжский', 'Приволжский'),
                      ('Советский', 'Советский'),
                      ('Авиастроительный', 'Авиастроительный'))
GEEKS_CHOICES_CATEGORY = (('Продажа', 'Продажа'),
                          ('Аренда', 'Аренда'))

class ApartmentForm(forms.Form):
    metro_name = forms.ChoiceField(label='Метро', required=False, choices=GEEKS_CHOICES_METRO,
                                   widget=forms.Select(attrs={'class': 'form-control'}))
    # required = False
    # queryset = Metro.objects.all(),
    # widget = forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}
    floor_number = forms.CharField(label='Этаж',
                              widget=forms.TextInput(attrs={'placeholder': 'этаж', 'class': 'form-control'}))
    metro_distance = forms.CharField(label='Путь до метро', required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'в мин. пешком', 'class': 'form-control'}))
    total_square = forms.CharField(label='Общая площадь',
                              widget=forms.TextInput(attrs={'placeholder': 'кв.м.', 'class': 'form-control'}))
    living_square = forms.CharField(label='Жилая площадь', required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'кв.м.', 'class': 'form-control'}))
    floor_total = forms.CharField(label='Всего этажей',widget=forms.
                                  TextInput(attrs={'placeholder': 'количество этажей', 'class': 'form-control'}))
    # count_room = forms.CharField(label='Комнат',widget=forms.
    #                              TextInput(attrs={'placeholder': 'количество комнат', 'class': 'form-control'}))
    count_room = forms.CharField(label='Комнат',
                                         widget=forms.TextInput(attrs={'class': 'form-control'}))
    material = forms.CharField(label='Материал',widget=forms.
                               TextInput(attrs={'placeholder': 'материал строения', 'class': 'form-control'}))
    # balcony_type = forms.CharField(label='Балкон',widget=forms.
    #                                TextInput(attrs={'placeholder': 'Тип балкона, количество', 'class': 'form-control'}))
    balcony_type = forms.CharField(label='Тип балкона', required=False,
                                         widget=forms.TextInput(attrs={'placeholder': 'Балкон, Лоджия, их количество',
                                                                       'class': 'form-control'}))

    is_home_appliances = forms.CharField(label='Техника',widget=forms.
                                         TextInput(attrs={'placeholder': 'С техникой, какая, без техники', 'class': 'form-control'}))

    is_furniture = forms.CharField(label='Мебель', widget=forms.
                                   TextInput(attrs={'placeholder': 'С мебелью, какая, без мебели', 'class': 'form-control'}))
    cost = forms.CharField(label='Стоимость', widget=forms.
                               TextInput(attrs={'placeholder': 'в руб.', 'class': 'form-control'}))
    currency = forms.CharField(label='Валюта', initial='руб',widget=forms.TextInput(attrs={'class': 'form-control'}))

    house_number = forms.CharField(label='Дом', widget=forms.
                               TextInput(attrs={'placeholder': 'номер дома', 'class': 'form-control'}))
    street = forms.CharField(label='Улица', widget=forms.
                               TextInput(attrs={'placeholder': 'street', 'class': 'form-control'}))
    city = forms.CharField(label='Населенный пункт', initial='Казань', widget=forms.
                               TextInput(attrs={'class': 'form-control'}))
    # area_city = forms.CharField(label='Район', widget=forms.
    #                            TextInput(attrs={'class': 'form-control'}))
    # area_city = forms.ModelChoiceField(label='Район', queryset = Area_city.objects.all(),
    #                                      widget=forms.Select(attrs={'class': 'form-control'}))
    area_city = forms.ChoiceField(label='Район', required=False, choices=GEEKS_CHOICES_AREA,
                                       widget=forms.Select(attrs={'class': 'form-control'}))
    advertising_object = forms.CharField(label='Краткая реклама', required=False, widget=forms.
                               TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание объекта', widget=forms.
                               Textarea(attrs={'class': 'form-control'}))
    # category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), label='Тип объявления', widget=forms.
    #                                           CheckboxSelectMultiple())
    category = forms.ChoiceField(label='Тип объявления', choices=GEEKS_CHOICES_CATEGORY,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    сreator = forms.CharField(label='Создатель', initial='user',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

class UpdateApartmentForm(forms.ModelForm):
    class Meta:
        model = Apartment
        exclude = ('metro_distance_number', 'year_public', 'month_public', 'day_public',
                   'time_public', 'url_object')
    # metro_name = forms.ChoiceField(label='Метро', required=False, choices=GEEKS_CHOICES_METRO,
    #                                widget=forms.Select(attrs={'class': 'form-control'}))
    metro_name = forms.ModelChoiceField(label='Метро', required=False, queryset=Metro.objects.all(),
                                        widget=forms.Select(attrs={'class': 'form-control'}))
    # metro_name = forms.CharField(label='Метро', required=False,
    #                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    floor_number = forms.CharField(label='Этаж',
                                   widget=forms.TextInput(attrs={'placeholder': 'этаж', 'class': 'form-control'}))
    metro_distance = forms.CharField(label='Путь до метро', required=False,
                                     widget=forms.TextInput(
                                         attrs={'placeholder': 'в мин. пешком', 'class': 'form-control'}))
    total_square = forms.CharField(label='Общая площадь',
                                   widget=forms.TextInput(attrs={'placeholder': 'кв.м.', 'class': 'form-control'}))
    living_square = forms.CharField(label='Жилая площадь', required=False,
                                    widget=forms.TextInput(attrs={'placeholder': 'кв.м.', 'class': 'form-control'}))
    floor_total = forms.CharField(label='Всего этажей', widget=forms.
                                  TextInput(attrs={'placeholder': 'количество этажей', 'class': 'form-control'}))
    count_room = forms.ModelChoiceField(label='Комнат', queryset=Room_count.objects.all(),
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    material = forms.ModelChoiceField(label='Материал', queryset=Material.objects.all(), widget=forms.
                               Select(attrs={'placeholder': 'материал строения', 'class': 'form-control'}))

    balcony_type = forms.ModelChoiceField(label='Тип балкона', required=False, queryset=Balcony.objects.all(),
                                   widget=forms.Select(attrs={'placeholder': 'Балкон, Лоджия, их количество',
                                                                'class': 'form-control'}))
    is_home_appliances = forms.CharField(label='Техника', widget=forms.
                                         TextInput(
        attrs={'placeholder': 'С техникой, какая, без техники', 'class': 'form-control'}))
    is_furniture = forms.CharField(label='Мебель', widget=forms.
                                   TextInput(
        attrs={'placeholder': 'С мебелью, какая, без мебели', 'class': 'form-control'}))
    cost = forms.CharField(label='Стоимость', widget=forms.
                           TextInput(attrs={'placeholder': 'в руб.', 'class': 'form-control'}))
    currency = forms.ModelChoiceField(label='Валюта', initial='руб', queryset=Currency.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    house_number = forms.CharField(label='Дом', widget=forms.
                                   TextInput(attrs={'placeholder': 'номер дома', 'class': 'form-control'}))
    street = forms.CharField(label='Улица', widget=forms.
                             TextInput(attrs={'placeholder': 'street', 'class': 'form-control'}))
    city = forms.ModelChoiceField(label='Населенный пункт', initial='Казань', queryset=Sity.objects.all(),widget=forms.
                           Select(attrs={'class': 'form-control'}))
    area_city = forms.ModelChoiceField(label='Район', required=False, queryset=Area_city.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    advertising_object = forms.CharField(label='Краткая реклама', required=False, widget=forms.
                                         TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(label='Описание объекта', widget=forms.
                                  Textarea(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='Тип объявления', choices=GEEKS_CHOICES_CATEGORY,
                                 widget=forms.Select(attrs={'class': 'form-control'}))
    сreator = forms.CharField(label='Создатель', initial='user',
                              widget=forms.TextInput(attrs={'class': 'form-control'}))







