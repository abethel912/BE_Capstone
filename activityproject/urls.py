from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from activities.views import ActivityViewSet

# Create a Router
router = routers.DefaultRouter()
# Register viewset with the router
router.register(r'activities', ActivityViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
]
