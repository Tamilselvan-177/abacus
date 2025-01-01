from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Dynamic path for starting a test based on the level
    path('start_test/<int:level>', views.start_test, name='start_test'),
    
    path('submit_test/', views.submit_test, name='submit_test'),
    path('details/<int:test_id>/', views.test_result, name='details'),
    
    # View result path
    path('result/', views.test_result, name='result'),
    
    # User Authentication paths
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='login_user'),
    
    # View previous test results
    path('view_previous_tests/', views.view_previous_tests, name='view_previous_tests'),
]
