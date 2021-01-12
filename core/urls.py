from django.urls import path
from . import views

app_name = 'core'


urlpatterns = [
    path('', views.IndexView.as_view(), name='index-page'),
    path('terms-and-conditions/', views.TermsView.as_view(), name='terms-page'),
]