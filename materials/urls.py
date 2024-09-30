from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials import views

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='course')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LessonListAPIView.as_view(), name='lessons-list'),
    path('create/', views.LessonCreateAPIView.as_view(), name='lessons-create'),
    path('<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lessons-detail'),
    path('<int:pk>/update/', views.LessonUpdateAPIView.as_view(), name='lessons-update'),
    path('<int:pk>/delete/', views.LessonDeleteAPIView.as_view(), name='lessons-delete'),
    # post subscription
    path('subscribe/', views.AssignCourse.as_view(), name='subscribe'),

] + router.urls
