"""
URL configuration for pasasalron project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views # importa las visitas de la app
from .views import tutpage, tutdetailview, addtutview
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'), # define la url raiz ('') y la vista asociada (views.home)
    path('about', views.about, name='about'),
    path('database', views.database, name='database'),

    path('database/accounts/register/', views.input, name='inputAccount'),
    path('database/accounts/register/redirect/', views.postAccount, name='postAccount'),
    #view all accounts
    path('database/accounts/', views.getAccount,name='getAccount'),
    #view account by id
    path('database/accounts/<int:id>', views.getAccount,name='getAccount'),
    #change account
    path('database/accounts/change/<int:id>', views.putAccount, name='updateAccount'),
    #view account by id
    path('database/accounts/change_register>/<int:id>', views.getAccount, name='updateRegister'),
    #delete
    path('database/accounts/delete/<int:id>', views.deleteAccount, name='deleteAccount'),

    path('tutorials', tutpage.as_view(), name='tutorials'),
    path('tutorials/article/<int:pk>', tutdetailview.as_view(), name='tutsdet'),
    path('tutorials/add_post', addtutview.as_view(), name='tutsadd'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)