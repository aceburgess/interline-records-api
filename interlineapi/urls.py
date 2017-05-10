"""interlineapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from rest_framework import routers
from interlineapi import views

from graphene_django.views import GraphQLView

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'videos', views.VideoViewSet)
router.register(r'general', views.GeneralViewSet, base_name='general')
router.register(r'site_settings', views.SiteSettingViewSet)
router.register(r'staff', views.StaffViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'announcements', views.AnnouncementViewSet)

# IF GRAPHENE {SCHEMA} is not defined in settings.py it can be defined here
# Folliwing line as an example
### from interlineapi.schema import schema

# ALSO....
# url pattern for graphql will have to look like so if schema is defined here:
### url(r'^graphql', GraphQLView.as_view(graphiql=True)),

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
