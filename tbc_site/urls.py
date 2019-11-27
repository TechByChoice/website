from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
#from models import TeamPage as team_page

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in

    url(r'^about/', TemplateView.as_view(template_name='home/about_page.html'), name="about"),
    url(r'^coc/', TemplateView.as_view(template_name='home/coc.html'), name="coc"),
    url(r'^diversity-statement/', TemplateView.as_view(template_name='home/diversity-statement.html'), name="diversity"),
    #url(r'^team/', team_page), name="team_page"),
    # TODO || REMOVE HARDCODED TEAM MEMBER NAME AND MAKE IT A VAR
    # TODO || PULL MEMBER INFO FROM OUT DB VS HARD CODING EVERYTHING
    url(r'^valerie', TemplateView.as_view(template_name='home/team_member_page.html'), name="teams"),
    url(r'^partners/', TemplateView.as_view(template_name='home/partners_page.html'), name="partners_page"),
    url(r'^team/', TemplateView.as_view(template_name='home/team_page.html'), name="team_page"),
    url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
