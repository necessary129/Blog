"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from default import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?:page/(?P<page>\d+)/)?$', views.index, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^contact/$', views.contact, name="contact"),
    url(r'^post/(?P<pk>\d+)/(?P<slug>[\w-]+)/$', views.post, name="post"),
    url(r'^mail/$', views.mail, name="mail"),
    url(r'^tag/(?P<slug>[\w-]+)/(?:page/(?P<page>\d+)/)?$', views.tag, name="tag")
]
