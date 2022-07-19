from django.contrib import admin

from cart.models import Order

class OrderAdmin(admin.ModelAdmin):
	list_display = ('client_name', 'phone', 'ids_str', 'full_price')


admin.site.register(Order, OrderAdmin)

