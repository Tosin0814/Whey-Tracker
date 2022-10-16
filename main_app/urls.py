from operator import ne
from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('whey/', views.WheyList.as_view(), name='whey_index'),
    path('whey/<int:whey_id>/', views.whey_detail, name='whey_detail'),
    path('whey/create', views.WheyCreate.as_view(), name='whey_create'),
    path('whey/<int:pk>/update/', views.WheyUpdate.as_view(), name='whey_update'),
    path('whey/<int:pk>/delete/', views.WheyDelete.as_view(), name='whey_delete'),

    path('whey/<int:whey_id>/add_customer_review/', views.add_customer_review, name='add_customer_review'),
    
    path('celebrities/', views.CelebList.as_view(), name = 'celeb_index'),
    path('celebrities/<int:pk>', views.CelebDetail.as_view(), name = 'celeb_detail'),
    path('celebrities/create', views.CelebCreate.as_view(), name = 'celeb_create'),
    path('celebrities/<int:pk>/update/', views.CelebUpdate.as_view(), name = 'celeb_update'),
    path('celebrities/<int:pk>/delete/', views.CelebDelete.as_view(), name = 'celeb_delete'),
    path('whey/<int:whey_id>/assoc_celeb/', views.assoc_celeb, name='assoc_celeb'),
    # path('whey/<int:whey_id>/assoc_celeb/<int:celebrity_id>/', views.assoc_celeb, name='assoc_celeb'),
    path('whey/<int:whey_id>/disassoc_celeb/<int:celebrity_id>/', views.disassoc_celeb, name='disassoc_celeb'),
    path('whey/<int:whey_id>/add_photo/', views.add_photo, name='add_photo'),
]