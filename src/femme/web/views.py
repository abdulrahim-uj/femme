from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from web.models import AboutClass


# Create your views here.
# def index(request):
#     return HttpResponseRedirect(reverse('web:test_redirect'));
#
# # RESPONSE REDIRECT
# def test(request):
#     return HttpResponse("Hello Django Again from test redirect");

def index(request):
    # all()  -- return -- queryset
    # filter() -- return -- queryset
    # exclude() -- return -- queryset
    # get() -- return -- object

    about_instances = AboutClass.objects.all()
    context = {
        "app_title": "Home",
        "about_instances": about_instances,
    }
    return render(request, 'web/index.html', context);