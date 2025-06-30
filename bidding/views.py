from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RequestBidSerializer
from .models import ProductBid
from .price_helper import adjusted_cpc

class BidView(APIView):
    def post(self, request):
        serializer = RequestBidSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            adjusted_cpc = adjusted_cpc(
                float(data['current_cpc']), float(data['target_roas'])
            )

            ProductBid.objects.create(
                product_id=data['product_id'],
                current_cpc=data['current_cpc'],
                target_roas=data['target_roas'],
                adjusted_cpc=adjusted_cpc
            )

            return Response({'adjusted_cpc': adjusted_cpc}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)