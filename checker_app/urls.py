from django.urls import path

from checker_app.views import index_view

urlpatterns = [
    path("", index_view, name='index')
]
