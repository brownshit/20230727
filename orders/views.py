from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Menu, Order
from .serializers import MenuSerializer, OrderSerializer
from django.shortcuts import render

#git
def index(request):
    return render(reqeust, 'index.html')

@api_view(['POST'])
def submit_order(request):
    phone_number = request.data.get('phoneNumber')
    menu = request.data.get('menu')
    total = request.data.get('total')

    # 데이터베이스에 저장하는 코드
    order = Order.objects.create(phone_number=phone_number, menu=menu, total=total)
    serializer = OrderSerializer(order)
    return Response(serializer.data)
#gpt
@api_view(['GET'])
def menu_list(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_to_cart(request):
    if request.method == 'POST':
        menu_id = request.data.get('menu_id')
        menu = Menu.objects.get(pk=menu_id)
        order = Order.objects.first()
        order.menu_items.add(menu)
        order.total_price += menu.price
        order.save()
        return Response({'message': 'Menu added to cart successfully.'})

@api_view(['POST'])
def remove_from_cart(request):
    if request.method == 'POST':
        menu_id = request.data.get('menu_id')
        menu = Menu.objects.get(pk=menu_id)
        order = Order.objects.first()
        order.menu_items.remove(menu)
        order.total_price -= menu.price
        order.save()
        return Response({'message': 'Menu removed from cart successfully.'})

@api_view(['POST'])
def checkout(request):
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')
        order = Order.objects.first()
        order.phone_number = phone_number
        order.save()
        # 결제 처리 등 추가적인 로직이 필요함
        return Response({'message': 'Order placed successfully.'})
