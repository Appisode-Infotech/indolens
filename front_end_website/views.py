from django.http import HttpResponse
from django.shortcuts import render, redirect

from indolens_admin.admin_controllers import orders_controller
from indolens_admin.admin_controllers.central_inventory_controller import get_central_inventory_product_single


def index(request):  # new
    return HttpResponse('<h1>WELCOME TO INDOLENS PUBLIC WEBSITE</h1>')


def customerOrderTracking(request, orderId):
    order_detail, status_code = orders_controller.get_order_details(orderId)
    order_track, track_status_code = orders_controller.get_order_track(orderId)
    print(order_track)
    return render(request, 'order_tracking/order_tracking.html', {"order_detail": order_detail['orders_details'],
                                                                  "order_track": order_track['order_track']})


def viewProductDetsils(request, productId):
    response, status_code = get_central_inventory_product_single(productId)
    return render(request, 'Products/viewProductDetails.html', {"product_data": response['product_data']})
