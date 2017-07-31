"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from core.views import LoginView, SignUpView, ProfileView, logout, AlunoListView, AlunoDetailView, home

urlpatterns = [
	#URL pra dar match, view
    url(r'^$', home, name='home'),
	url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^signup/', SignUpView.as_view(), name='signup'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),
    url(r'^aluno/(?P<pk>\d+)$', AlunoDetailView.as_view(), name='aluno'),
    url(r'^alunos/', AlunoListView.as_view(), name='alunos'),
    url(r'^logout$', logout, name='logout'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
