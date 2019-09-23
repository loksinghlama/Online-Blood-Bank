from django.urls import path
from . import views
urlpatterns = [
path('', views.home, name='home'),
path('stock/', views.stock, name='stock'),
path('request/', views.request, name='request'),
path('stockinput/', views.stockinput, name='stockinput'),
path('requestlist/', views.requestlist, name='requestlist'),
path('donatedlist/', views.donatedlist, name='donatedlist')
]
