from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MenuView, BookingView
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'restaurant'

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingView)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',views.MenuView.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/',include(router.urls), name='booking'),
    path('api-token-auth/',obtain_auth_token),
    path('message/', views.msg),
]