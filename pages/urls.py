# from django.urls import path
# from .views import HomePageView


# urlpatterns = [
#     ("", HomePageView.as_view(), name="home"),
# ]

from django.urls import path
from .views import landing_view, home_view

urlpatterns = [
    path('', landing_view, name='landing'),
    path('home/', home_view, name='home'),
    path('landing/', LandingPageView.as_view(), name='landing'),
]
