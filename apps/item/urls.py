from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import ItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet, basename='categories')
router.register('items', ItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls))
]