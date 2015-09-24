from django.conf.urls import url

urlpatterns = [
    # Examples:
    # url(r'^$', 'codenames.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$/', 'spygame.views', namespace="spygame"),

]
