from django.urls import path
from study_tracker.views import show_tracker, create_assignment, show_xml, show_json
from study_tracker.views import register, login_user, logout_user


app_name = 'study_tracker'

urlpatterns = [
    path('', show_tracker, name='show_tracker'),
    path('create', create_assignment, name='create_assignment'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),

    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat


    path('login/', login_user, name='login'),

    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat




]