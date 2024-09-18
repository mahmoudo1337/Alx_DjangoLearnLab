from django.shortcuts import render

# Create your views here.
# notifications/views.py

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
# notifications/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Notification
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

class MarkNotificationReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        notification = get_object_or_404(Notification, pk=pk, recipient=request.user)
        notification.read = True
        notification.save()
        return Response({"detail": "Notification marked as read."}, status=status.HTTP_200_OK)
