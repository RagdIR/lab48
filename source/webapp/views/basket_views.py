from django.views.generic import ListView
from webapp.models import Basket


class BasketView(ListView):
    template_name = 'basket/basket_view.html'
    context_object_name = 'basket'
    model = Basket

    # for product in products:
    #     if product in Basket:
    #         basket.product.amount +1


