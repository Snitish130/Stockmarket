
from django.urls import path
from stockapp.views import home , login , signup , signout ,add_stock , searchstock , stockDetail , export_data_xls

urlpatterns = [
    path('' , home , name='home'),
    path('stock/<str:slug>' , stockDetail , name='stockdetail'),
    path('login' , login , name = 'login'),
    path('signup' , signup , name = 'signup'),
    path('logout' , signout ),
    path('search-stock' , searchstock , name = 'search_stock'),
    path('add-stock' , add_stock ),
    path('stock/<str:slug>/export-data', export_data_xls, name='export_data'),

]
