from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from bidding.models import ProductBid

class BidViewTests(APITestCase):
    def test_post_bid_success(self):
        response = self.client.post(reverse('bid'), {
            "product_id": "demo123",
            "current_cpc": "1.50",
            "target_roas": "200"
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['adjusted_cpc'], 3.0)
        self.assertEqual(ProductBid.objects.count(), 1)

    def test_post_invalid_bid(self):
        response = self.client.post(reverse('bid'), {
            "product_id": "bad",
            "current_cpc": "-1.0",
            "target_roas": "100"
        }, format='json')

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['adjusted_cpc'], 0.0)