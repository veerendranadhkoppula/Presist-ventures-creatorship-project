from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TestAPIView(APIView):
    def get(self, request):
        data = {"message": "Hello from Django!"}
        return Response(data, status=status.HTTP_200_OK)


class HomePageView(TemplateView):
    template_name = 'home.html'

class DailyReminderView(TemplateView):
    template_name = 'daily_reminder.html'
