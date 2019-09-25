from django.urls import path
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative_url_templates, name='relative_url_templates'),
    path('other/', views.other, name='other'),
]