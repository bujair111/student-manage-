from django.urls import path
from . import views

app_name = 'common'


urlpatterns = [
    path('common',views.common,name = 'common')

]