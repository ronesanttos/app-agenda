from django.urls import path
from contact import views
app_name = 'contact'

urlpatterns = [
    path('',views.index, name='index'),
    path('search/', views.search, name='search'),
    
    #contacts (CRUD)
    path('contact/<int:contact_id>/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
    path('contact/<int:contact_id>/update/', views.update_contact, name='update'),
    path('contact/<int:contact_id>/delete/', views.delete, name='delete'),
    
    #user 
    path('user/create/', views.register, name='register'),
    path('user/login/', views.login, name='login'),
    path('user/logout/', views.logout, name='logout'),
    path('user/update/', views.update, name='update'),
]
