"""online_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first, name='first'),
    path('index',views.index, name='index'),
    path('reg/', views.reg, name='reg'),
    path('reg/register_view/', views.register_view, name='register'),
    path('login/', views.login, name='login'),
    path('login/login_view', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    path('about-us/', views.about_us, name='about-us'),
    path('our-services/', views.our_services, name='our-services'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('viewuser', views.viewuser, name='viewuser'),
    path('update_status/<int:user_id>/<str:status>/', views.update_status, name='update_status'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('add_election', views.add_election, name='add_election'),
    path('add_legislature', views.add_legislature, name='add_legislature'),
    path('add_constituency', views.add_constituency, name='add_constituency'),
    path('add_candidate', views.add_candidate, name='add_candidate'),
    path('add_voterlist', views.add_voterlist, name='add_voterlist'),
    path('view_voterlist', views.view_voterlist, name='view_voterlist'),
    path('update_voterlist_status/<int:voterlist_id>/<str:status>/', views.update_voterlist_status, name='update_voterlist_status'),
    path('view_candidate', views.view_candidate, name='view_candidate'),
    path('publish_result', views.publish_result, name='publish_result'),
    path('results', views.results, name='results'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
