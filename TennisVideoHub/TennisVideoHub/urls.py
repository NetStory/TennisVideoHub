"""
URL configuration for TennisVideoHub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
]


"""
TODO
Assign: JLZ

Task: notes这是在干啥:将/videos/开头的url请求给videos处理

Why? 一个项目有多个app时 需要分发请求给不同的app处理

Deliverable: 写完
"""
urlpatterns += [
    path('videos/', include('videos.urls')),
]

from django.views.generic import RedirectView

"""
TODO
Assign: JLZ

Task: notes这是在干啥:如果访问的url是根目录 则重定向到/videos/

Why? 因为功能在videos里 直接访问根目录就404了

Deliverable: 写完
"""
urlpatterns += [
    path('', RedirectView.as_view(url='/videos/')),
]

from django.conf import settings
from django.conf.urls.static import static

"""
TODO
Assign: JLZ

Task: notes这是在干啥:在开发环境下，让 Django 能提供静态文件

Why?不是特别懂

Deliverable: 写完
"""
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)