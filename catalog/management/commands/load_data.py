import json
from django.core.management.base import BaseCommand
from django.db import connection
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Загружает тестовые данные из фикстур'

    def handle(self, *args, **options):
        self.stdout.write('🔄 Очистка базы данных...')
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE catalog_category CASCADE;')
            cursor.execute('TRUNCATE TABLE catalog_product CASCADE;')

        self.stdout.write('📦 Загрузка категорий...')
        with open('fixtures/categories.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Category.objects.create(
                    id=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description']
                )

        self.stdout.write('📦 Загрузка продуктов...')
        with open('fixtures/products.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data:
                Product.objects.create(
                    id=item['pk'],
                    name=item['fields']['name'],
                    description=item['fields']['description'],
                    price=item['fields']['price'],
                    category_id=item['fields']['category'],
                    image=item['fields']['image'] if item['fields'].get('image') else None,
                    created_at=item['fields']['created_at'],
                    updated_at=item['fields']['updated_at']
                )

        self.stdout.write('🎉 Данные успешно загружены!')
