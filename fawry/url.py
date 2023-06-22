from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('mainPage', views.mainPage, name='mainPage'),
    path('details/<int:obj_id>', views.details, name='details'),
    path('update_expenses' , views.update_expenses , name='update_expenses'),
    path('add_transaction/<int:obj_id>' , views.add_transaction , name='add_transaction')
]
