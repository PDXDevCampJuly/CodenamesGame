from django.conf.urls import url
from spygame import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'codenames.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$/', 'views.get_spy_page', name="get_spy_page"),
    url(r'^$/', 'views.get_spymaster_page', name="get_spymaster_page"),
    url(r'^$/', 'views.join_or_create', name="join_or_create"),
    url(r'^$/', 'views..spy_or_spymaster', name="spy_or_spymaster"),
]
