from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from indolens_admin.admin_controllers import orders_controller
from indolens_admin.admin_controllers.central_inventory_controller import get_central_inventory_product_single
from indolens_admin.admin_controllers.graphs_and_statistics import get_own_vs_franchise_sales_stats


def index(request):  # new
    return HttpResponse('<h1>WELCOME TO INDOLENS PUBLIC WEBSITE</h1>')


def customerOrderTracking(request, orderId):
    order_detail, status_code = orders_controller.get_order_details(orderId)
    order_track, track_status_code = orders_controller.get_order_track(orderId)
    print(order_track)
    return render(request, 'order_tracking/order_tracking.html', {"order_detail": order_detail['orders_details'],
                                                                  "order_track": order_track['order_track']})


def viewProductDetails(request, productId):
    response, status_code = get_central_inventory_product_single(productId)
    return render(request, 'Products/viewProductDetails.html', {"product_data": response['product_data']})


@api_view(['POST'])
def get_franchise_vs_ownStore_sale(request):
    start_date = datetime.strptime(request.data['fromDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(request.data['toDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    Controller_response, status_code = get_own_vs_franchise_sales_stats(start_date, end_date)

    response = {
        "ownStoreSales": Controller_response['own_store_sale_stats'],
        "franchiseStoreSales": Controller_response['franchise_store_sale_stats']
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_customer_analytics(request):
    start_date = datetime.strptime(request.data['fromDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(request.data['toDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    Controller_response, status_code = get_own_vs_franchise_sales_stats(start_date, end_date)

    response = {
        "ownStoreSales": Controller_response['own_store_sale_stats'],
        "franchiseStoreSales": Controller_response['franchise_store_sale_stats']
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_order_analytics(request):
    start_date = datetime.strptime(request.data['fromDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(request.data['toDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    Controller_response, status_code = get_own_vs_franchise_sales_stats(start_date, end_date)

    response = {
        "ownStoreSales": Controller_response['own_store_sale_stats'],
        "franchiseStoreSales": Controller_response['franchise_store_sale_stats']
    }
    return JsonResponse(response, status=200)
