from django.urls import path
from mainapp.views import UserView, StatsView, count_view, TaxDetailView, tax_add, company_add, latest_news, contacts
from users.views import Register
from users.views import UserDetailView


app_name = 'mainapp'
urlpatterns = [
    path('', UserView.as_view(), name='mainpage'),
    path('company_detail/<int:pk>', StatsView.as_view(), name='company_detail'),
    path('company_add/', company_add, name='company_add'),
    path('count/', count_view, name='count'),
    path('tax_add/', tax_add, name='tax_add'),
    path('latest_news/', latest_news, name='latest_news'),
    path('contacts/', contacts, name='contacts'),
    path('tax_detail/<int:pk>', TaxDetailView.as_view(), name='tax_detail'),
]
