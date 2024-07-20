from django.urls import path
from .views import HomePageView, DailyReminderView
from .views import TestAPIView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('daily-reminder/', DailyReminderView.as_view(), name='daily_reminder'),
    path('api/test/', TestAPIView.as_view(), name='test-api'),
]
