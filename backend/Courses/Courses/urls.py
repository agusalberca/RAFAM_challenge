from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api import views
router = routers.DefaultRouter()
router.register(r'users', views.Custom_userViewSet, "users")
router.register(r'courses', views.CourseViewSet)
router.register(r'lessons', views.LessonViewSet)
router.register(r'friendships', views.FriendshipViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]