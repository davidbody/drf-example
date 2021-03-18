from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .my_api import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('total_views/', views.TotalViewsView.as_view(), name="total-views"),
    path('admin/', admin.site.urls),
]
