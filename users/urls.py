from django.urls import path
from users.apps import UsersConfig
from users import views

app_name = UsersConfig.name


urlpatterns = [
    path('update/<int:pk>/', views.UserUpdateAPIView.as_view(), name='user-update'),
    path('create/', views.UserCreateAPIView.as_view(), name='user-create'),
    path('delete/<int:pk>/', views.UserDeleteAPIView.as_view(), name='user-delete'),
    path('', views.UserListAPIView.as_view(), name='user-list'),
    path('<int:pk>/', views.UserRetrieveAPIView.as_view(), name='user-detail'),
    #  Payments API
    path('payments/', views.PaymentsAPIView.as_view(), name='payment-list'),
    # get token
    path('token/', views.UserTokenObtainPairView.as_view(),name='user-token'),
]