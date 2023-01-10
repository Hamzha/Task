from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add-deals/', views.addDeals, name='add-deals'),
    path('admin-category/', views.adminCategory, name='admin-category'),
    path('business-account/', views.businessAccount, name='business-account')

]
