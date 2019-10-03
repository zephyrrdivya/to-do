from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView

# for rest framework

APPEND_SLASH = True

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),
    path('', include('user.urls')),
    path('api-auth/', include('rest_framework.urls'))
    # path('accounts/login',
    #      LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('accounts/logout',
    #      LogoutView.as_view(), name='logout'),
]
