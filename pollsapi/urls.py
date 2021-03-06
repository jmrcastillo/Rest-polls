"""pollsapi URL Configuration

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
from django.urls import include, path
from django.contrib import admin
# core api
from rest_framework.documentation import include_docs_urls
# rest swagger
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Polls API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    # rest swagger
    path('swagger-docs/', schema_view),
    # coreapi
    path('docs/', include_docs_urls(title='Polls API')),
]
