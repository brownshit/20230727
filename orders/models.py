from django.db import models
#gpt-1
# class Order(models.Model):
#     phone_number = models.CharField(max_length=20)
#     # Add other fields here (e.g., menu items, quantity, total price, etc.)

#     def __str__(self):
#         return self.phone_number

class Menu(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')

class Order(models.Model):
    phone_number = models.CharField(max_length=15)

    menu_items = models.ManyToManyField(Menu)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    menu = models.CharField(max_length=100)

    def __str__(self):
        return f'Order by {self.phone_number} for {self.menu}'
# # Create your models here.
# # models.py 파일에 전화번호를 저장할 모델을 정의합니다.
# class PhoneNumber(models.Model): 
#     phone_number = models.CharField(max_length=11)

#     def __str__(self):
#         return self.phone_number
#     pass


# #api models
# class apiModel(models.Model):
#     #필드 정의
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     def __str__(self):
#         return self.field1