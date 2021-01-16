from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('user', UserAPI, basename='UserAPI')
router.register('book', BookAPI, basename='BookAPI')
router.register('payment', PaymentAPI, basename='PaymentAPI')
router.register('category', CategoryAPI, basename='CategoryAPI')
router.register('branch', BranchAPI, basename='BranchAPI')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<int:pk>/', include(router.urls)),
    path('api/<str:pk>/', include(router.urls)),
    path('api/<slug:pk>/', include(router.urls)),
]
