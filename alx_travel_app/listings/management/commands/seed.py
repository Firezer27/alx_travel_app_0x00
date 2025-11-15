from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random


class Command(BaseCommand):
    help = "Seed the database with sample listings"

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            username="testuser",
            defaults={"email": "test@example.com"}
        )

        sample_listings = [
            {
                "title": "Modern Apartment in City Center",
                "description": "Beautiful 2 bedroom apartment close to all amenities.",
                "price_per_night": 55.00,
                "location": "Addis Ababa"
            },
            {
                "title": "Cozy Guest House",
                "description": "Quiet guest house located in a peaceful neighborhood.",
                "price_per_night": 35.00,
                "location": "Bahir Dar"
            },
            {
                "title": "Luxury Villa with Pool",
                "description": "5-star accommodation with private pool and garden.",
                "price_per_night": 120.00,
                "location": "Hawassa"
            },
        ]

        for item in sample_listings:
            Listing.objects.create(
                title=item["title"],
                description=item["description"],
                price_per_night=item["price_per_night"],
                location=item["location"],
                owner=user,
            )

        self.stdout.write(self.style.SUCCESS("Database seeding completed!"))
