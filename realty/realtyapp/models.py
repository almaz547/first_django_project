from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        if self.name == 'sale':
            self.name = 'Продажа'
        if self.name == 'rent':
            self.name = 'Аренда'
        return self.name

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

class Metro(models.Model):
    name = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.name

class Room_count(models.Model):
    name = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.name

class Balcony(models.Model):
    name = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.name

class Street(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Sity(models.Model):
    name = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.name

class Area_city(models.Model):
    name = models.CharField(max_length=32, blank=True)
    def __str__(self):
        return self.name

class Images(models.Model):
    image = models.ImageField(upload_to='apartments', blank=True, null=True)

class Apartment(models.Model):

    url_object = models.URLField(blank=True)
    metro_name = models.ForeignKey(Metro, blank=True, null=True, on_delete=models.CASCADE)
    metro_distance = models.CharField(max_length=50, blank=True)
    metro_distance_number = models.CharField(max_length=32, blank=True)
    total_square = models.CharField(max_length=32, blank=True)
    living_square = models.CharField(max_length=32, blank=True)
    floor_number = models.CharField(max_length=32, blank=True)
    floor_total = models.CharField(max_length=32, blank=True)
    count_room = models.ForeignKey(Room_count, blank=True, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, blank=True, on_delete=models.CASCADE)
    balcony_type = models.ForeignKey(Balcony, blank=True, on_delete=models.CASCADE)
    is_home_appliances = models.CharField(max_length=32, blank=True)
    is_furniture = models.CharField(max_length=32, blank=True)
    year_public = models.CharField(max_length=32, blank=True)
    month_public = models.CharField(max_length=32, blank=True)
    day_public = models.CharField(max_length=32, blank=True)
    time_public = models.CharField(max_length=16, blank=True)
    cost = models.CharField(max_length=32, blank=True)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=32, blank=True)
    street = models.ForeignKey(Street, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(Sity, blank=True, on_delete=models.CASCADE)
    area_city = models.ForeignKey(Area_city, blank=True, on_delete=models.CASCADE)
    advertising_object = models.CharField(max_length=70, blank=True)
    description = models.CharField(max_length=150, blank=True)
    category = models.ManyToManyField(Category)
    сreator = models.CharField(max_length=36, blank=True)
    image = models.ForeignKey(Images, blank=True, null=True, on_delete=models.CASCADE)

class Images_url(models.Model):

    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    url_image = models.URLField()




class Message_user(models.Model):
    name = models.CharField(max_length=32)
    message = models.TextField()
    email = models.EmailField()
    create = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=16, blank=True)
