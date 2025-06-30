from rest_framework import serializers

class RequestBidSerializer(serializers.Serializer):
    product_id = serializers.CharField()
    current_cpc = serializers.DecimalField(max_digits=10, decimal_places=2)
    target_roas = serializers.DecimalField(max_digits=6, decimal_places=2)