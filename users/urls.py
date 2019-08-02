from django.urls import include, path, re_path

from . import views


urlpatterns = [
    path('', views.UserListView.as_view()),
    path('edit/<int:pk>/', views.UserRetrieveUpdateAPIView.as_view())
]
