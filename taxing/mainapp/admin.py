from django.contrib import admin
from mainapp.models import Percent, Types, Months, Taxes, Payment, Fines, Company, Year, Count


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('type_of_company', 'type_of_company', 'name', 'created', 'not_paid',
                    'has_fine', 'paid_before', 'for_militiary',)
    list_display_links = ('name', )


@admin.register(Percent)
class PercentAdmin(admin.ModelAdmin):
    list_display = ('percent_id', 'amount')


@admin.register(Fines)
class FinesAdmin(admin.ModelAdmin):
    list_display = ('fine_id', 'summ')


@admin.register(Types)
class TypesAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'name')


@admin.register(Months)
class MonthsAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Taxes)
class TaxesAdmin(admin.ModelAdmin):
    list_display = ('tax', 'time')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('sqrt',)


@admin.register(Year)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('year',)


@admin.register(Count)
class CountAdimn(admin.ModelAdmin):
    list_display = ('summs',)