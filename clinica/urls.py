from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs da app core
    path('', include('core.urls')),

    # Login e logout (se quiser manter no projeto principal)
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('paciente-info/<int:paciente_id>/', views.paciente_info, name='paciente_info'),
 
]