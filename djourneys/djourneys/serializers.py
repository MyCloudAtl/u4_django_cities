from rest_framework import serializers
from .models import City, Attraction, Review

class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    attraction = serializers.HyperlinkedRelatedField(
        view_name='attraction_detail',
        read_only=True
    )
    attraction_id = serializers.PrimaryKeyRelatedField(
        queryset=Attraction.objects.all(),
        source='attraction'
    )
    class Meta:
        model = Review
        fields = ('id', 'attraction','attraction_id', 'reviewer_name', 'comment', 'reviewer_company',)

class AttractionSerializer(serializers.HyperlinkedModelSerializer):
    reviews = serializers.HyperlinkedRelatedField(
        view_name='review_detail',
        read_only=True
    )
    reviews = ReviewSerializer(
        many=True,
        read_only=True
    )
    city = serializers.HyperlinkedRelatedField(
        view_name='city_detail',
        read_only=True
    )
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(),
        source='city'
    )
    class Meta:
        model = Attraction
        fields = ('id', 'city','city_id', 'name', 'category', 'description', 'image_url', 'reviews',)


class CitySerializer(serializers.HyperlinkedModelSerializer):
    attractions = AttractionSerializer(
        many=True,
        read_only=True
    )
    city_url = serializers.ModelSerializer.serializer_url_field(
        view_name='city_detail'
    )
    class Meta:
        model = City
        fields = ('id', 'city_url', 'name', 'state', 'population', 'attractions',)