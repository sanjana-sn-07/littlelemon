from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import MenuView, BookingView
from rest_framework.authtoken.views import obtain_auth_token

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingView)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/',views.MenuView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/',include(router.urls)),
    path('api-token-auth/',obtain_auth_token),
    path('message/', views.msg),
]