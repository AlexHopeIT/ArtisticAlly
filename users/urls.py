from django.contrib.auth import views as auth_view
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.urls import path

from . import views
from .forms import RussianLoginForm


class CustomLoginView(auth_view.LoginView):
    authentication_form = RussianLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = False

    def get_success_url(self):
        return reverse_lazy('profile')


def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('index'))
    else:
        return HttpResponseRedirect(reverse('index'))


urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', CustomLoginView.as_view(authentication_form=RussianLoginForm,
                                           template_name='users/login.html',
                                           redirect_authenticated_user=False), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
