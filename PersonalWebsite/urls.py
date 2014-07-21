from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('PersonalWebsite.views',
    url(r'^$', 'infoPage.load', {"page":"home"}, name="home"),
    url(r'^home/?|index/?$', 'infoPage.load', {"page":"home"}, name="home"),

    url(r'^projects/?$', 'infoPage.load', {"page":"projects"}, name="projects"),
    url(r'^websites/?$', 'infoPage.load', {"page":"websites"}, name="websites"),
    url(r'^hackathons/?$', 'infoPage.load', {"page":"hackathons"},name="hackathons"),

    url(r'^photos/?$', 'infoPage.load', {"page":"photos"}, name="photos"),
    url(r'^gallery/(?P<page>\w+)/$', 'gallery.gallery'),

    url(r'^more/?$', 'infoPage.load', {"page":"more"}, name="more"),

    url(r'^vim(?:tip)?/?$', 'infoPage.load', {"page":"vimTip"}, name="vimTip"),

    # External Redirects
    url(r'^blog/?$',
        RedirectView.as_view(url="http://blog.caseyfalk.com"),
        name="blog"),
    url(r'^\.?vimrc/?$',
        RedirectView.as_view(url="https://github.com/cfalk/vimrc-and-colorscheme"),
        name="vimrc"),

)

