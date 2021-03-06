from django.conf.urls.static import static
from django.urls import path, include
from .views import Home, About, Resume

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('resume/', Resume.as_view(), name='resume'),
]
