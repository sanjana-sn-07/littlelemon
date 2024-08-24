from django.shortcuts import render
from .models import Menu, Booking
from .serializers import menuSerializer, bookingSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import Booking
from .serializers import bookingSerializer, menuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class BookingView(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    
class MenuView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class =menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})
