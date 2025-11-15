from rest_framework import serializers
from .models import Listing, Booking


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in', 'check_out']


class ListingSerializer(serializers.ModelSerializer):
    bookings = BookingSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = [
            'id',
            'title',
            'description',
            'price_per_night',
            'location',
            'owner',
            'bookings'
        ]
