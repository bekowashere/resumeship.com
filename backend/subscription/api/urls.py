from django.urls import path
from subscription.api.views import (
    PlanListAPIView,
    PlanDetailAPIView,
    
    SubscriptionListAPIView,
    SubscriptionDetailAPIView,

    SubscribeView
)

app_name = 'subscription'

urlpatterns = [
    path('plans/', PlanListAPIView.as_view(), name='plan_list'),
    path('plans/<str:id>', PlanDetailAPIView.as_view(), name='plan_detail'),

    path('subscriptions/', SubscriptionListAPIView.as_view(), name='subscription_list'),
    path('subscriptions/<str:id>', SubscriptionDetailAPIView.as_view(), name='subscription_detail'),

    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
]