from django.urls import path
from loginform import views 

urlpatterns = [
    path('login/',views.login,name='login')
]