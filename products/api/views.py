from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from urllib.parse import unquote
from django.conf import settings
from random import shuffle

from algoliasearch.search_client import SearchClient

import stripe

stripe.api_key = settings.STRIPE_SK_TEST

from ..models import Product
from ..serializers import ProductSerializer, ProductPreviewSerializer


@api_view(['GET'])
def get_all_products(request, *args, **kwargs):
    try:
        products = Product.objects.all()
    except:
        return Response({"details": "error grabbing products"}, status=500)
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def create_product(request, *args, **kwargs):
    # TODO: update product creation to account for new fields
    data = dict(request.POST)

    product = Product.objects.create(
        name=data['name'][0], 
        description=data['description'][0], 
        price=float(data['price'][0]), 
        active_discount=float(data['active_discount'][0]), 
        carbon_footprint=float(data['carbon_footprint'][0]), 
        image_link=data['image_link'][0],  
        sku=data['sku'][0], 
        tags=data['tags'],
        category=data['category'][0]
    )
    
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=201)


@api_view(['GET'])
def get_product_by_id(request, id, *args, **kwargs):
    try: 
        product = Product.objects.get(id=id)
    except:
        return Response({'details': 'no product found'}, status=400)
        
    
    serializer = ProductSerializer(product)   
    
    return Response(serializer.data, status=200)

@api_view(['DELETE'])
def delete_product(request, id, *args, **kwargs):
    try: 
        product = Product.objects.get(id=id)
    except:
        return Response({'details': 'no product found'}, status=400)
    
    product.delete()
    
    return Response({"details", "product deleted successfully"}, status=200)


@api_view(['PUT'])
def update_product(request, *args, **kwargs):
    try: 
        product = Product.objects.get(id=id)
    except:
        return Response({'details': 'no product found'}, status=400)
    
    product.update(request.data)
    
    serializer = ProductSerializer(product)
    
    return Response(serializer.data, status=200)

@api_view(["GET"])
def get_recommended_preview(request, *args, **kwargs):
    try:
        products = Product.objects.recommended()
    except Exception as e:
        print(e)
    
    serializer = ProductPreviewSerializer(products, many=True)
    shuffle(serializer.data)
    return Response(serializer.data[:10], status=200)


@api_view(["GET"])
def get_recommended_products(request, *args, **kwargs):
    try:
        products = Product.objects.recommended()
    except Exception as e:
        print(e)
    
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data, status=200)

@api_view(["GET"])
def get_product_by_handle(request, handle, *args, **kwargs):
    try: 
        product = Product.objects.filter(handle=handle).first()
    except Exception as e:
        print(e)
        return Response({'details': 'no products found'}, status=400)
    
    serializer = ProductSerializer(product)
    
    
    return Response(serializer.data, status=200)


@api_view(["GET"])
def get_category_preview(request, category, *args, **kwargs):
    try: 
        products = Product.objects.category(unquote(category))
        # products = Product.objects.filter(category__name=unquote(category)).all()[:10]
    except Exception as e:
        return Response({'details': 'no products found in this category'}, status=400)
    
    serializer = ProductPreviewSerializer(products, many=True)
    
    shuffle(serializer.data)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def get_product_by_category(request, category, *args, **kwargs):
    try: 
        products = Product.objects.category(unquote(category))
    except Exception as e:
        return Response({'details': 'no products found in this category'}, status=400)
    
    serializer = ProductSerializer(products, many=True)
    
    return Response(serializer.data, status=200)


@api_view(['POST'])
def create_checkout_session(request, *args, **kwargs):
    
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=request.data,
            mode='payment',
            payment_method_types= ['card'],
            success_url= settings.CLIENT_URL + '/#/success',
            cancel_url= settings.CLIENT_URL + '/#/cancel',
        )
    except Exception as e:
        print('ERROR:', e)
        return Response({'detail': e}, status=500)

    return Response(checkout_session.url, status=303)


    
@api_view(['GET'])
def create_index(request, *args, **kwargs):
    client = SearchClient.create(settings.ALGOLIA_APP_ID, settings.ALGOLIA_API_KEY)

    index = client.init_index('products')    
    
    productCount = Product.objects.exclude(title=None).exclude(body=None).count()
      
    
    i = 0
    cap = 200
    count = 0
    currData = []
    
    
    
    while i < productCount:
        products = Product.objects.exclude(title=None).exclude(body=None).all().distinct()[i:i + cap]  
        serializer = ProductPreviewSerializer(products, many=True) 
        currData = serializer.data
            
        
        try:
            index.save_objects(currData, {
                'autoGenerateObjectIDIfNotExist': True,
            })
        except Exception as e:
            print(e)
            return Response({'detail': 'Error saving index chunk ' + str(count)}, status=500)
        else:
            print(f'Chunk {count} saved to algolia index')
            
        i += cap
        count += 1
            
        

    
        
    
    return Response({'detail': 'Index successfully created for product'}, 200)


@api_view(['GET', 'DELETE'])
def delete_duplicates(request, *args, **kwargs):
    for product in Product.objects.values_list('title', flat=True).distinct():
        if not product:
            continue
        print(product)
        Product.objects.filter(pk__in=Product.objects.filter(title=product).values_list('id', flat=True)[1:]).delete()
        
    return Response({'detail': 'Duplicate products successfully deleted'}, 200)