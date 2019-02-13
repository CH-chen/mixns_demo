"""mixns_demo URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from app01 import views

#第三种url简写
#简写第一步
from rest_framework import routers

routers = routers.DefaultRouter()
routers.register(r"books001",views.BookViewSet) #books001为URL前缀



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publisher/$', views.PublsherMixView.as_view()),
    # url(r'^publisher/(\d+)/$', views.PublisherDetailView.as_view()), #不加超链接
    url(r'^publisher/(?P<pk>\d+)/', views.PublisherDetailMix.as_view(), name="publisher_detail"),


    url(r'^book/$', views.BookMixView.as_view()),
    url(r'^book/(?P<pk>\d+)/$', views.BookDetailMix.as_view()),

    ##**********第二种*******
    url(r'^publishers/$', views.PublsherGenView.as_view()),
    url(r'^publishers/(?P<pk>\d+)/$', views.PublisherDetailGen.as_view()),

    url(r'^books/$', views.BookGenView.as_view(),name="book_list"),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailGen.as_view(),name="book_detail"),

    ##*****第三种 这种还可以简写
    # url(r'^books1/$', views.BookViewSet.as_view({"get":"list","post":"create"}),name="book_list"),
    # url(r'^books1/(?P<pk>\d+)/$', views.BookViewSet.as_view({
    #             'get': 'retrieve',
    #             'put': 'update',
    #             'patch': 'partial_update',
    #             'delete': 'destroy'
    #         }),name="book_detail"),


    ##简写第二步
    url(r'^', include(routers.urls)),


]

#简写默认生成如下url
# # ^books001/$ [name='book-list']
# ^ ^books001\.(?P<format>[a-z0-9]+)/?$ [name='book-list']
# ^ ^books001/(?P<pk>[^/.]+)/$ [name='book-detail']
# ^ ^books001/(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='book-detail']