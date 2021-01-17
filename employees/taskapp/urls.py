from django.urls import path, include
from rest_framework.routers import DefaultRouter
from taskapp import views
from rest_framework.urlpatterns import format_suffix_patterns


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'role', views.RoleViewSet)

# router.register(r'comment', views.CommentViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   
	path('comments/', views.CommentList.as_view()),
	path('roles/', views.RoleDetail.as_view()),

	]
