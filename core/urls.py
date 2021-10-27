from django.urls import path
from .views import ClientHomeView, searchView

urlpatterns = [
    path('', ClientHomeView.as_view(), name='home'),
    path('search', searchView, name='search'),

]
