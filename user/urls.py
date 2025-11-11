from django.urls import path
from . import views

# http://127.0.0.1:8000/index

urlpatterns = [
    path('login/', views.login, name='login'),
	path('register/', views.register, name='register'),
	path('logout/', views.logout, name='logout'),
	path('odeme/', views.odeme_sayfasi, name='odeme_sayfasi'),
    path("odeme-bildirim/", views.odeme_bildirim, name="odeme_bildirim"),
    path('chat_api/', views.chat_api, name='chat_api'),

]