from django.contrib import admin
from django.urls import path, include, re_path
from CRUDUsers import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/users/$', views.userLista),
    re_path(r'^api/user/([0-9]+)$', views.usersDetail),
    re_path(r'^api/enderecos/$', views.enderecoLista),
    re_path(r'^api/user/([0-9]+)/enderecos/$', views.userEndereco),
    re_path(r'^api/user/([0-9]+)/endereco/([0-9]+)$', views.userEnderecoEdit)
]

