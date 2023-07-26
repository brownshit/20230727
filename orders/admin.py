from django.contrib import admin

# Register your models here.
#gpt-1
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone_number',)  # 관리자 페이지에서 보여질 필드 목록
    search_fields = ('phone_number',)  # 검색 기능을 제공할 필드 목록

admin.site.register(Order, OrderAdmin)