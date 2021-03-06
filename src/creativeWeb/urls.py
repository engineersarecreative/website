from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #Links home page to home function
    url(r'^$', 'signUps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #Links /thank-you page to thankyou function
    url(r'^thankyou/$', 'signUps.views.thankyou', name='thankyou'),
    url(r'^logout/$', 'signUps.views.logout', name='logout'),
    #Allows admin page to function
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)