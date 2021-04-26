# from django.contrib.admin.views.decorators import staff_member_required
# from django.db.models import Avg, Count, F, Sum
# from django.db.models.functions import ExtractDay, ExtractMonth, ExtractYear
from django.http import JsonResponse

from .models import Prices  # , Products

# from django.shortcuts import render


# from utils.charts import months, colorPrimary, colorSuccess, colorDanger, generate_color_palette, get_year_dict


def get_filter_options(request):
    grouped_products = Prices.objects.values("product_number").distinct()
    # grouped_prices = Prices.objects.annotate(day=ExtractDay('timestamp'), product='product_number',
    #                                          avg_price=Avg('price_excl_shipping')).order_by('-day')

    options = [product["product_number"] for product in grouped_products]

    return JsonResponse(
        {
            "options": options,
        }
    )


#
#
# @staff_member_required
# def get_sales_chart(request, year):
#     purchases = Purchase.objects.filter(time__year=year)
#     grouped_purchases = purchases.annotate(price=F('item__price')).annotate(month=ExtractMonth('time'))\
#         .values('month').annotate(average=Sum('item__price')).values('month', 'average').order_by('month')
#
#     sales_dict = get_year_dict()
#
#     for group in grouped_purchases:
#         sales_dict[months[group['month']-1]] = round(group['average'], 2)
#
#     return JsonResponse({
#         'title': f'Sales in {year}',
#         'data': {
#             'labels': list(sales_dict.keys()),
#             'datasets': [{
#                 'label': 'Amount ($)',
#                 'backgroundColor': colorPrimary,
#                 'borderColor': colorPrimary,
#                 'data': list(sales_dict.values()),
#             }]
#         },
#     })
