from django.test import TestCase, Client
from .models import Apartment, Images
from mixer.backend.django import mixer
from userapp.models import ApartmentUser

class ViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.client_2 = Client()

    def test_statuses(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/sale/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/rent/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/new_buildings/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/message/')
        self.assertEqual(response.status_code, 302)



        response = self.client.get('/create_apart/')
        self.assertEqual(response.status_code, 302)


        response = self.client.get(f'/apartment/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/updata_apart/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/delete_confirm/')
        self.assertEqual(response.status_code, 404)

        response = self.client.get('/delete_image_confirm/')
        self.assertEqual(response.status_code, 404)

        # Создаем объявление
        apartment = mixer.blend(Apartment)
        response = self.client.get(f'/apartment/{apartment.pk}/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/updata_apart/{apartment.pk}/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get(f'/delete_confirm/{apartment.pk}/')
        self.assertEqual(response.status_code, 200)



    def test_login_required(self):
        user = ApartmentUser.objects.create_user(username='test_user', email='test@test.com', password='test1234567test')
        user2 = ApartmentUser.objects.create_user(username='test_user2', email='test@test2.com',
                                                 password='test1234567test2')

        # Отправляем подтверждение для первого
        response = self.client.get('/user/confirmat/test@test.com/')
        self.assertEqual(response.status_code, 200)

        # Они не вошли
        response = self.client.get('personal_area/')
        self.assertEqual(response.status_code, 404)
        response_2 = self.client_2.get('personal_area/')
        self.assertEqual(response_2.status_code, 404)

        # Логиним первого
        self.client.login(username='test_user', password='test1234567test')
        response = self.client.get('/personal_area/')
        self.assertEqual(response.status_code, 200)

        # Второй не вошел
        response_2 = self.client_2.get('personal_area/')
        self.assertEqual(response_2.status_code, 404)