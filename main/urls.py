from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('tracker/', views.tool_main_section, name='tool_page'),
    path('tracker/reset/', views.tool_reset_section, name='tool_reset_func'),
    path('tracker/calculate/', views.tool_calculate_section, name='tool_calculate_func')
]
