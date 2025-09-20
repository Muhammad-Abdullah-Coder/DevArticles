# from django.url import path
# from django import SignUpView

# urlpatterns = [
#     path("signup/",SignUpView.as_view(), name="signup"),
# ]


from django.urls import path
from .views import SignUpView, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
