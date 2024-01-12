from django.http import HttpResponse
from django.shortcuts import render, redirect

from indolens_admin.admin_controllers import orders_controller


def index(request):  # new
    return HttpResponse('<h1>WELCOME TO INDOLENS PUBLIC WEBSITE</h1>')


def customerOrderTracking(request, orderId):
    order_detail, status_code = orders_controller.get_order_details(orderId)
    order_track, track_status_code = orders_controller.get_order_track(orderId)
    print(order_track)
    return render(request, 'order_tracking/order_tracking.html', {"order_detail": order_detail['orders_details'],
                                                                  "order_track": order_track['order_track']})
