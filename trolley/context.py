from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from store.models import Product


def trolley_contents(request):

    trolley_items = []
    total = 0
    items_count = 0
    delivery_difference = settings.FREE_DELIVERY_MIN_SPEND - total

    trolley = request.session.get('trolley', {})
    for product_id, quantity in trolley.items():
        product = get_object_or_404(Product, pk=product_id)

        if product.special_price:
            total += product.special_price * quantity
        else:
            total += product.price * quantity
        items_count += quantity
        trolley_items.append({
            'product_id': product_id,
            'product': product,
            'total': total,
            'quantity': quantity,
            'items_count': items_count,
        })
        delivery_difference -= total

    if delivery_difference > 0:
        delivery_charge = Decimal(total * settings.APPLY_DELIVERY_PERCENTAGE)
    else:
        delivery_charge = 0

    free_delivery_min_spend = settings.FREE_DELIVERY_MIN_SPEND
    grand_total = total + delivery_charge

    context = {
        'trolley_items': trolley_items,
        'total': total,
        'items_count': items_count,
        'delivery_difference': delivery_difference,
        'free_delivery_min_spend': free_delivery_min_spend,
        'delivery_charge': delivery_charge,
        'grand_total': grand_total,
    }

    return context
