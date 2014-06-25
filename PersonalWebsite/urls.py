from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('PersonalWebsite.views',
    url(r'^$', 'infoPage.load', {"page":"home"}, name="home"),
    url(r'^home|index$', 'infoPage.load', {"page":"home"}, name="home"),

    url(r'^projects/?$', 'infoPage.load', {"page":"projects"}, name="projects"),
    url(r'^websites/?$', 'infoPage.load', {"page":"websites"}, name="websites"),
    url(r'^hackathons/?$', 'infoPage.load', {"page":"hackathons"},name="hackathons"),
    url(r'^more/?$', 'infoPage.load', {"page":"more"}, name="more"),

    #TODO:Change to a separate function.
    url(r'^blog/?$', 'infoPage.load', {"page":"blog"}, name="blog"),

    url(r'^admin/', include(admin.site.urls)),
)
