import json
import os.path

from django.core.management import BaseCommand

from coursecorrect import settings
from mainapp.models import Product


class Command(BaseCommand):
    help = 'populates data with json file'

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'product.json')
        print(path)

        self.stdout.write(
            self.style.SUCCESS('starting to ingest data')
        )

        with open(path) as file:
            products = json.load(file)

            for product in products:
                Product.objects.create(
                    product_name=product['product_name'],
                    product_code=product['product_code'],
                    product_price=product['product_price'],
                    product_description=product['product_description'],
                    product_image='images/default.jpg',
                    sale=product['sale'],
                )

        self.stdout.write(
            self.style.SUCCESS('finished ingesting data')
        )
