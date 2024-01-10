from django.contrib import admin
from django.urls import path, include

from users.views import indexpage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexpage, name='index'),
    path('user/', include('users.urls')),
]
