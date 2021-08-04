from rest_framework import routers
from django.contrib import admin
from django.urls import path, include

from . import views

router = routers.DefaultRouter()
#router.register(r'query', views.QueryDashboard)


urlpatterns = [
	path('getCounts', views.get_counts),
]
