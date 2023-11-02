from rest_framework import serializers
from .models import Product
class ProductSerializer(serializers.ModelSerializer):
    offert = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'content', 'price', 'sale_price', 'offert']

    def get_offert(self, instance):
        if not hasattr(instance, 'id'):
            return None
        else:
            return instance.get_discount()