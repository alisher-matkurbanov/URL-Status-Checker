from django.urls import path

from checker_app.views import index_view, check_url, switch_url_pause_status

urlpatterns = [
    path("", index_view, name='index'),
    path("ajax/check_url", check_url, name='update_url'),
    path("ajax/update_url_pause_status", switch_url_pause_status,
         name='update_url_pause_status')
]
