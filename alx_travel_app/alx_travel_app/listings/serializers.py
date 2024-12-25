from rest_framework import serializers
from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'created_at']

class BookingSerializer(serializers.ModelSerializer):
    listing = ListingSerializer()

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'user', 'check_in_date', 'check_out_date', 'created_at']

    def validate(self, data):
        if data['check_in_date'] >= data['check_out_date']:
            raise serializers.ValidationError("Check-in date must be before check-out date.")
        return data