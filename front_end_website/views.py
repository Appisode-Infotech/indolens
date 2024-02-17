from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from indolens_admin.admin_controllers import orders_controller


def index(request):  # new
    return HttpResponse('<h1>WELCOME TO INDOLENS PUBLIC WEBSITE</h1>')


def customerOrderTracking(request, orderId):
    order_detail, status_code = orders_controller.get_order_details(orderId)
    order_track, track_status_code = orders_controller.get_order_track(orderId)
    print(order_track)
    return render(request, 'order_tracking/order_tracking.html', {"order_detail": order_detail['orders_details'],
                                                                  "order_track": order_track['order_track']})


@api_view(['POST'])
def get_franchise_vs_ownStore_sale(request):
    print("case1")
    response = {
        "ownStoreSales": [
            100, 200, 300, 300, 300, 250, 200, 200, 200, 200, 200, 500, 500, 500, 600,
            700, 800, 900, 1000, 100, 850, 600, 600, 600, 400, 200, 200, 300, 300, 300, 500
        ],
        "franchiseStoreSales": [
            200, 200, 100, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 50, 200, 400, 600,
            600, 600, 800, 1000, 700, 400, 450, 500, 600, 700, 650, 600, 550, 200
        ]
    }
    return JsonResponse(response, status=200)
