from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view

from indolens_admin.admin_controllers import orders_controller
from indolens_admin.admin_controllers.central_inventory_controller import get_central_inventory_product_single
from indolens_admin.admin_controllers.graphs_and_statistics import get_own_vs_franchise_sales_stats, get_customer_stats, \
    get_orders_stats, get_store_sales_stats, get_store_customer_stats, get_store_orders_stats


def index(request):  # new
    return HttpResponse('<h1>WELCOME TO INDOLENS PUBLIC WEBSITE</h1>')


def customerOrderTracking(request, orderId):
    order_detail, status_code = orders_controller.get_order_details(orderId)
    order_track, track_status_code = orders_controller.get_order_track(orderId)
    return render(request, 'order_tracking/order_tracking.html', {"order_detail": order_detail['orders_details'],
                                                                  "order_track": order_track['order_track'],
                                                                  "store_details": order_track['store_details']})


def viewProductDetails(request, productId):
    response, status_code = get_central_inventory_product_single(productId)
    return render(request, 'Products/viewProductDetails.html', {"product_data": response['product_data']})


@api_view(['POST'])
def get_franchise_vs_ownStore_sale_analytics(request):
    start_date = datetime.strptime(request.data['fromDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(request.data['toDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    Controller_response, status_code = get_own_vs_franchise_sales_stats(start_date, end_date)

    response = {
        "ownStoreSales": Controller_response['own_store_sale_stats'],
        "franchiseStoreSales": Controller_response['franchise_store_sale_stats']
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_store_sale_analytics(request):
    start_date = datetime.strptime(request.data['fromDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(request.data['toDate'], '%m/%d/%Y').strftime('%Y-%m-%d')
    store_type = request.data['storeType']
    store_id = request.data['storeId']
    Controller_response, status_code = get_store_sales_stats(start_date, end_date, store_type, store_id)

    response = {
        "store_sale_stats": Controller_response['store_sale_stats'],
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_customer_analytics(request):
    days = int(request.data['type'])
    Controller_response, status_code = get_customer_stats(days)

    response = {
        "list": Controller_response['customer_stats'],
        "interval": days
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_store_customer_analytics(request):
    days = int(request.data['type'])
    store_type = request.data['storeType']
    store_id = request.data['storeId']
    Controller_response, status_code = get_store_customer_stats(days, store_type, store_id)

    response = {
        "list": Controller_response['customer_stats'],
        "interval": days
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_order_analytics(request):
    days = int(request.data['type'])
    Controller_response, status_code = get_orders_stats(days)

    response = {
        "list": Controller_response['order_stats'],
        "interval": days
    }
    return JsonResponse(response, status=200)


@api_view(['POST'])
def get_store_order_analytics(request):
    days = int(request.data['type'])
    store_type = request.data['storeType']
    store_id = request.data['storeId']
    Controller_response, status_code = get_store_orders_stats(days, store_type, store_id)

    response = {
        "list": Controller_response['order_stats'],
        "interval": days
    }
    return JsonResponse(response, status=200)
