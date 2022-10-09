from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse('web:test_redirect'));


def test(request):
    return HttpResponse("Hello Django Again from test redirect");
