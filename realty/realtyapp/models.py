from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name

class Metro(models.Model):
    name = models.CharField(max_length=32, blank=True)

class Room_count(models.Model):
    name = models.CharField(max_length=32, blank=True)

class Material(models.Model):
    name = models.CharField(max_length=32, blank=True)

class Balcony(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)

class Currency(models.Model):
    name = models.CharField(max_length=32, blank=True)

class Street(models.Model):
    name = models.CharField(max_length=32)

class Sity(models.Model):
    name = models.CharField(max_length=32, blank=True)

class Area_city(models.Model):
    name = models.CharField(max_length=32, blank=True)



class Apartment(models.Model):

    url_object = models.URLField()
    metro_name = models.ForeignKey(Metro, blank=True, null=True, on_delete=models.CASCADE)
    metro_distance = models.CharField(max_length=50, blank=True)
    metro_distance_number = models.CharField(max_length=32, blank=True)
    total_square = models.CharField(max_length=32, blank=True)
    living_square = models.CharField(max_length=32, blank=True)
    floor_number = models.CharField(max_length=32, blank=True)
    floor_total = models.CharField(max_length=32, blank=True)
    count_room = models.ForeignKey(Room_count, blank=True, null=True, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, blank=True, null=True, on_delete=models.CASCADE)
    balcony_type = models.ForeignKey(Balcony, blank=True, null=True, on_delete=models.CASCADE)
    is_home_appliances = models.CharField(max_length=32, blank=True)
    is_furniture = models.CharField(max_length=32, blank=True)
    year_public = models.CharField(max_length=32, blank=True)
    month_public = models.CharField(max_length=32, blank=True)
    day_public = models.CharField(max_length=32, blank=True)
    time_public = models.CharField(max_length=16, blank=True)
    cost = models.CharField(max_length=32, blank=True)
    currency = models.ForeignKey(Currency, blank=True, null=True, on_delete=models.CASCADE)
    house_number = models.CharField(max_length=32, blank=True)
    street = models.ForeignKey(Street, blank=True, null=True, on_delete=models.CASCADE)
    city = models.ForeignKey(Sity, blank=True, null=True, on_delete=models.CASCADE)
    area_city = models.ForeignKey(Area_city, blank=True, null=True, on_delete=models.CASCADE)
    advertising_object = models.CharField(max_length=70, blank=True)
    description = models.CharField(max_length=150, blank=True)
    category = models.ManyToManyField(Category)
    # image = models.ForeignKey(Images, blank=True, null=True, on_delete=models.CASCADE)

class Images(models.Model):
    # image = models.ImageField(upload_to='apartaments', blank=True, null=True)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
    url_image = models.URLField()




class Message_user(models.Model):
    name = models.CharField(max_length=32)
    message = models.TextField()
    email = models.EmailField()
    create = models.DateTimeField(auto_now_add=True)
    telefone = models.CharField(max_length=16, blank=True, null=True)
