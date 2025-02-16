from django.core.management.base import BaseCommand
from listings.models import Listing
from faker import Faker
from django.db import transaction

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with a given number of listings'

    def add_arguments(self, parser):
        # Add a command-line argument 'num' to specify the number of listings
        parser.add_argument('num', type=int, help='Number of listings to create')

    @transaction.atomic
    def handle(self, *args, **kwargs):
        # Retrieve the 'num' argument
        num_listings = kwargs['num']

        # Create the specified number of listings
        try:
            for _ in range(num_listings):
                Listing.objects.create(
                    title=fake.catch_phrase(),
                    description=fake.text(),
                    price_per_night=fake.random_int(min=50, max=500),
                    location=fake.city(),
                )

            self.stdout.write(self.style.SUCCESS(f'{num_listings} listings created successfully!'))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {str(e)}'))
            raise


