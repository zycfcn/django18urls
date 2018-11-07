"""django18urls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from testurls import views

# 后面加上 '/$' django 会强制在url 加上 '/'
# 比如: 输入http://127.0.0.1:8000/2018/01   按回车再看url 会在后面加上 '/'

urlpatterns = [
    # 首页
    url(r'^$', views.index),
    # 文章列表
    url(r'^articles/list',views.articlelist),
    # 按年份获取文章列表 {4}  表达只能是四个数字
    url(r'^articles/([0-9]{4})/$', views.articleyeara),
    # 按月份获取文章列表 {2}  表达只能是二个数字
    url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.articlemonthb),
    # 你可能有这样的需求，想给url 参数命名，像下面这样 '+' 代表匹配 1个到无数个
    url(r'^article/(?P<id>[0-9]+).html', views.articlecontent),
    # 两个命名参数，再在views 打乱顺序获取
    url(r'^articles/page(?P<page>[0-9]+)/(?P<num>[0-9]+)', views.articlepagelist),
    # 按文章分类查找文章列表
    url(r'^articles/label-(?P<label>\w+)/$', views.articlelabel),
    # url(r'^admin/', include(admin.site.urls)),
]
