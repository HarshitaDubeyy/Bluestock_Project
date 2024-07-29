from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    box = serializers.CharField(max_length=6,default='')
    name = serializers.CharField(max_length=255,default='Not Issued')
    Brand = serializers.CharField(max_length=255,default='Not Issued')
    Price_Band = serializers.CharField(max_length=100,default='Not Issued')
    Open = serializers.CharField(max_length=100,default='Not Issued')
    Close = serializers.CharField(max_length=100,default='Not Issued')
    Issue_size= serializers.CharField(max_length=100,default='Not Issued')
    Issue_Type= serializers.CharField(max_length=100,default='Not Issued')
    Listing_Date= serializers.CharField(max_length=100,default='Not Issued')

    def create(self, validated_data):
        return Item.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.Brand = validated_data.get('Brand', instance.Brand)
        instance.Price_Band = validated_data.get('Price_Band', instance.Price_Band)
        instance.Open = validated_data.get('Open', instance.Open)
        instance.Close = validated_data.get('Close', instance.Close)
        instance.Issue_size = validated_data.get('Issue_size', instance.Issue_size)
        instance.Issue_Type = validated_data.get('Issue_Type', instance.Issue_Type)
        instance.Listing_Date = validated_data.get('Listing_Date', instance.Listing_Date)
        instance.save()
        return instance

    class Meta:
        model = Item
        fields = '__all__'
