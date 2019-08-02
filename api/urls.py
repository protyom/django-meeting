from django.urls import include, path, re_path
from allauth.account.views import ConfirmEmailView

from .views import null_view, complete_view, email_test, change_meeting

urlpatterns = [
    path('users/', include('users.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

    re_path(r'^rest-auth/registration/account-email-verification-sent/', null_view,
            name='account_email_verification_sent'),
    # re_path(r'^rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
    #         ConfirmEmailView.as_view(), name='account_confirm_email'),
    re_path(r'^rest-auth/registration/complete/$', complete_view, name='account_confirm_complete'),
    re_path(r'^rest-auth/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        null_view, name='password_reset_confirm'),
    path('test_email/', email_test),
    path('meetings/', include('meetings.urls')),
    path('join/<int:pk>/', change_meeting)
]