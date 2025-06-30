from celery import shared_task
from django.utils.timezone import now
from datetime import timedelta
from .models import ProductBid

@shared_task
def daily_budget_audit():
    seven_days_ago = now() - timedelta(days=7)
    bids = ProductBid.objects.filter(calculated_at__gt=seven_days_ago)
    flagged = []

    for bid in bids:
        diff = abs(bid.adjusted_cpc - bid.current_cpc)
        if diff > 0.20 * bid.current_cpc:
            flagged.append(bid)

    print(f"Daily Budget Audit Report: {len(flagged)} bids flagged with >20% CPC difference.")