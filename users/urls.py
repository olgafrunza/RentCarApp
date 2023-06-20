from django.urls import path, include
from .views import RegisterView, logout


urlpatterns = [
    path('logout/', logout),
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
]
