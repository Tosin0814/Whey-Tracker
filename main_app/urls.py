from operator import ne
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('whey/', views.WheyList.as_view(), name='index'),
    # path('whey/<int:pk>/', views.WheyDetail.as_view(), name='detail'),
    path('whey/<int:whey_id>/', views.whey_detail, name='detail'),
    path('whey/create', views.WheyCreate.as_view(), name='whey_create'),
    path('whey/<int:pk>/update/', views.WheyUpdate.as_view(), name='whey_update'),
    path('whey/<int:pk>/delete/', views.WheyDelete.as_view(), name='whey_delete'),

    path('whey/<int:whey_id>/add_customer_review/', views.add_customer_review, name='add_customer_review'),
]