from django.contrib.auth import views as auth_view
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import path

from . import views


def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html',
                                               redirect_authenticated_user=False), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout')
]
