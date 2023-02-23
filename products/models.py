from django.db import models
from django.db.models import Q

from vendors.models import Vendor
from categories.models import Category
from urllib.parse import unquote

# Create your models here.
class ProductQuerySet(models.QuerySet):
    def recommended(self):
        return self.filter(Q(recommended=True) & ~Q(vendor_name=None) & ~Q(title=None)).distinct()[:10]
    
    def category(self, category):
        return self.filter(Q(category__name=category) & ~Q(title=None))[:10]


class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)  
    
    def recommended(self):
        return self.get_queryset().recommended()
    
    def search(self, query):
        return self.get_queryset().search(query)
    
    def category(self, category):
        return self.get_queryset().category(category)


class Product(models.Model):
    objects = ProductManager()
    
    # Product details
    handle = models.CharField(max_length=200)
    title = models.CharField(max_length=500, null=True, blank=True)
    body = models.TextField(max_length=500, null=True, blank=True)
    vendor_name = models.TextField(max_length=1000, null=True, blank=True)
    
    type = models.CharField(max_length=400, null=True, blank=True)
    tags = models.CharField(max_length=2500, null=True, blank=True)
    published = models.BooleanField(default=False, null=True)

    category = models.ForeignKey(Category, max_length=40, related_name='products', db_column="product_category", on_delete=models.SET_NULL, null=True)
    
    active_discount = models.DecimalField(max_digits=2, decimal_places=2, default=0, null=True)
    carbon_footprint = models.DecimalField(max_digits=6, decimal_places=3, null=True)
    
    option1_name = models.CharField(max_length=500, null=True, blank=True)
    option1_value = models.CharField(max_length=500, null=True, blank=True)
    option2_name = models.CharField(max_length=500, null=True, blank=True)
    option2_value = models.CharField(max_length=500, null=True, blank=True)
    option3_name = models.CharField(max_length=500, null=True, blank=True)
    option3_value = models.CharField(max_length=500, null=True, blank=True)
    
    
    
    # Variants
    variant_SKU = models.CharField(max_length=200, null=True, blank=True)
    variant_grams = models.DecimalField(max_digits=10, decimal_places = 2, null=True, blank=True)
    variant_inventory_tracker = models.CharField(max_length=512, null=True, blank=True)
    variant_inventory_qty = models.IntegerField(null=True, blank=True)
    variant_inventory_policy = models.CharField(max_length=512, null=True, blank=True)
    variant_fulfillment_service = models.CharField(max_length=40, null=True, blank=True)
    variant_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    variant_compare_at_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    variant_requires_shipping = models.BooleanField(default=True, null=True, blank=True)
    variant_taxable = models.BooleanField(default=True, null=True, blank=True)
    variant_barcode = models.CharField(max_length=60, null=True, blank=True)
    variant_weight_unit = models.CharField(max_length=4, null=True, blank=True)
    variant_tax_code = models.CharField(max_length=30, null=True, blank=True)
    
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    
    # images
    image_src = models.URLField(null=True, max_length=500)
    variant_image = models.URLField(null=True, blank=True, max_length=500)
    image_position = models.IntegerField(null=True)
    image_alt_text = models.TextField(default="No alt text found", null=True, blank=True)
    
    # SEO and Gift Cards
    gift_card = models.BooleanField(default=False, null=True, blank=True)
    SEO_title = models.CharField(max_length=60, null=True, blank=True)
    SEO_description = models.TextField(max_length=500, null=True, blank=True)
    
    # Goole Shopping
    google_shopping_google_product_category = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_gender = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_age_group = models.CharField(max_length=60, null=True, blank=True)
    
    google_shopping_MPN = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_adWords_grouping = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_adWords_labels = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_condition = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_custom_product = models.CharField(max_length=40, null=True, blank=True)
    
    
    google_shopping_custom_label0 = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_custom_label1 = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_custom_label2 = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_custom_label3 = models.CharField(max_length=40, null=True, blank=True)
    google_shopping_custom_label4 = models.CharField(max_length=40, null=True, blank=True)

    # options
    timestamp = models.DateTimeField(auto_now_add=True, null=True)
    recommended = models.BooleanField(default=False, null=True)
    
    source = models.CharField(max_length=300, null=True, blank=True)
    
    
    def __str__(self):
        return self.title or self.handle
    
    
    

