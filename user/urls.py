from django.urls import path
from user import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "user"  # 테스트코드


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="sign_up_view"),  # /user/signup/
    path(
        "verify-email/b'<str:uidb64>'/<str:token>/",
        views.VerifyEmailView.as_view(),
        name="verify-email",
    ),  # /user/verify-email/b'<str:uidb64>'/<str:token>/
    path(
        "reactivation/", views.ActivateAccountView.as_view(), name="reactivation"
    ),  # /user/reactivation/
    path(
        "login/", views.CustomTokenObtainPairView.as_view(), name="login_view"
    ),  # /user/login/
    # path("refresh/", TokenRefreshView.as_view(), name="token_refresh"), # /user/refresh/

    path(
        "<int:user_id>/", views.ProfileView.as_view(), name="profile_view"
    ),  # /user/<int:user_id>/
    path(
        "password/email/", views.PasswordResetView.as_view(), name="password_reset"
    ),  # 비밀번호 찾기 (이메일 보내기)
    path(
        "auth/password/reset/b'<str:uidb64>'/<str:token>/",
        views.PasswordTokenCheckView.as_view(),
        name="password_reset_confirm",
    ),  # 비밀번호 재설정 토큰 확인
    path(
        "password/reset/",
        views.SetNewPasswordView.as_view(),
        name="password_reset_confirm",
    ),  # 비밀번호 재설정
    # path("password/email/", views.PasswordResetView.as_view(), name="password_reset"),  # /user/password/email/ 비밀번호 찾기 (이메일 보내기)
    # path("password/check/", views.PasswordTokenCheckView.as_view(), name="password_reset_confirm"),  # /user/password/check/ 비밀번호 재설정 토큰 확인
    # path("password/reset/", views.SetNewPasswordView.as_view(), name="password_reset_confirm"),  # /user/password/reset/ 비밀번호 재설정
    path(
        "<int:user_id>/follow/", views.FollowView.as_view(), name="follow_view"
    ),  # user/<int:user_id>/follow/
    path("check/", views.DailyCheckView.as_view(), name="daily_check_view"),  # 출석체크
]