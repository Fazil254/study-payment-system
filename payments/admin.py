from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display  = ('name', 'email', 'course', 'amount', 'payment_status', 'date')
    list_filter   = ('payment_status', 'course')
    search_fields = ('name', 'email', 'course')
    ordering      = ('-date',)
