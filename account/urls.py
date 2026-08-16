from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup_page'),
    path('signin/', views.signin, name='signin_page'),
    path('signin/admin/', views.signin_for_admin, name='signin_admin_page'),
    path('signout/', views.signout, name='signout_system'),
    path('dashboard/', views.profile, name='profile_page'),
    path('dashboard/update/acc', views.update_acc_info, name='update_acc_info'),
    path('dashboard/update/pass', views.update_acc_password, name='update_acc_password'),
    path('dashboard/update/body/', views.update_body_info, name='update_body_info'),
    path('dashboard/report/<int:id>', views.view_reports_details, name='view_report')
]
