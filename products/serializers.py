from rest_framework import serializers
from vendors.serializers import VendorSerializer
from .models import Product
from reviews.models import Review
from reviews.serializers import ReviewSerializer


class ProductPreviewSerializer(serializers.ModelSerializer):
    median_rating = serializers.SerializerMethodField(read_only=True)
    
    # review_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = [
            'title',
            'handle',
            'variant_price',
            'vendor_name',
            'median_rating',
            'active_discount',
            # 'review_count',
            'image_src',
            'carbon_footprint',    
        ]
    
    # def get_review_count(self, obj):
    #     return len(obj.reviews.all())
    
    
    
    def get_median_rating(self, obj):
        mid = obj.reviews.count() // 2
        
        if mid == 0:
            return 0
        if obj.reviews.count() % 2 == 0:
            return (list(obj.reviews.all())[mid] + list(obj.reviews.all())[mid - 1]) / 2
        
        return list(obj.reviews.all())[mid] 


class ProductSerializer(serializers.ModelSerializer):
    vendor = VendorSerializer(read_only=True)
    reviews = serializers.SerializerMethodField(read_only=True)
    median_rating = serializers.SerializerMethodField(read_only=True)
    # average_rating = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'handle',
            'body',
            'variant_price',
            'variant_SKU',
            'vendor',
            'median_rating',
            'active_discount',
            'variant_weight_unit',
            'variant_grams',
            # 'average_rating'
            'reviews',
            'review_count',
            'image_src',
            'carbon_footprint',
            'timestamp',     
            
        ]
    

    def get_median_rating(self, obj):
        mid = obj.reviews.count() // 2
        
        if mid == 0:
            return 0
        if obj.reviews.count() % 2 == 0:
            return (list(obj.reviews.all())[mid] + list(obj.reviews.all())[mid - 1]) / 2
        
        return list(obj.reviews.all())[mid]
    
    def get_average_rating(self, obj):
        sum = 0
        for review in obj.reviews:
            sum += review.rating
            
        return sum / len(obj.reviews)
    
    def get_review_count(self, obj):
        return len(obj.reviews.all())
    
    def get_reviews(self, obj):
        reviews = Review.objects.filter(product_id=obj.id).all()
        
        serializer = ReviewSerializer(reviews, many=True)
        
        return serializer.data
        
                   
    
    
    

