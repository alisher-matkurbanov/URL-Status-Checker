from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


@staff_member_required
def index_view(request):
    return render(request, "index.html")
