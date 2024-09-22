from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials import views

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet, basename='courses')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.LessonCreateAPIView.as_view(), name='lessons-create'),
    path('', views.LessonListAPIView.as_view(), name='lessons-list'),
] + router.urls
