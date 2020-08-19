from django.urls import path

from .views import (
    LogInView,  SignUpView, LogOutView, ChangePasswordView,
    RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView,Request_list, detail, UpdateRequest, Admin_Request_list,
    NewRequest
)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),

    path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),
    path('adminrequests/',Admin_Request_list,name="admin_requests"),
    path('requests/',Request_list,name="requests"),
    path("newrequests/" ,NewRequest, name="New_request" ),
    path("requestdetail/<int:id>/",detail.as_view(), name="detail"),
    path("updaterequest/<int:id>/",UpdateRequest, name="update_request"),
    path('change/password/', ChangePasswordView.as_view(), name='change_password')
]
