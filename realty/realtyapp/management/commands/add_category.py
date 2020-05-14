from django.core.management.base import BaseCommand
from realtyapp.models import Category




class Command(BaseCommand):

    def handle(self, *args, **options):
        Category.objects.create(name='rent')
        Category.objects.create(name='sale')

