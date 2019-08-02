from django.urls import include, path, re_path
from .views import register, confirm_email, edit_user, login, meetings, logout

urlpatterns = [
    path('registration/', register, name="register"),
    re_path(r'confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name="my_confirm_email"),
    path('edit/', edit_user, name="edit_user"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('', meetings, name="home"),
]
