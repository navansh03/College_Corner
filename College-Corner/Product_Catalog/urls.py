from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'Product_Catalog'

urlpatterns = [
    path('', login_required(views.product_list.as_view()), name='ProductList'),
]
