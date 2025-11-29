from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


from core.views import agendar_corte, dashboard, fazer_logout 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', agendar_corte, name='agendar'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    
    # AQUI ESTÁ O SEGREDO: Tem que ser 'fazer_logout', não 'auth_views.LogoutView'
    path('logout/', fazer_logout, name='logout'),
]