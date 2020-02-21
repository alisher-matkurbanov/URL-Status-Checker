from django.contrib.admin.views.decorators import staff_member_required
import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from checker_app.models import URL
import requests


@staff_member_required
def index_view(request):
    urls = URL.objects.all()
    json_urls = [
        {
            "is_paused": 1 if url.is_paused == True else 0,
            "check_interval": url.check_interval,
            "id": url.id,
            "text": url.text,
            "response_status": url.response_status,
        }
        for url in urls
    ]
    print(json_urls)
    return render(request, "index.html", context={'urls': json_urls})


def check_url(request):
    url_id = int(request.POST["url_id"][0])
    try:
        url = URL.objects.get(id=url_id)
    except URL.DoesNotExist:
        return JsonResponse(data={
            "is_deleted": 1,
            "url_id": url_id,
        })
    if not url.is_paused:
        try:
            response_status = requests.head(url.text).status_code
        except requests.ConnectionError:
            response_status = 404
        url.response_status = response_status
        url.save()
    return HttpResponse(json.dumps({
        "is_deleted": 0,
        "url_id": url.id,
        "response_status": url.response_status,
        "check_interval": url.check_interval,
        "is_paused": 1 if url.is_paused == True else 0
    }), content_type="application/json")


def switch_url_pause_status(request):
    url_id = request.POST["url_id"][0]
    try:
        url = URL.objects.get(id=url_id)
        url.is_paused = not url.is_paused
        url.save()
    except URL.DoesNotExist:
        return JsonResponse(data={
            "is_deleted": 1,
            "url_id": url_id,
        })
    return HttpResponse(
        json.dumps({
            "status": "resume" if url.is_paused else "pause",
            "url_id": url_id
        }),
        content_type='application/json'
    )