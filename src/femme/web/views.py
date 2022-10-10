# from django.http.response import HttpResponse, HttpResponseRedirect
# from django.urls import reverse


# Create your views here.
# def index(request):
#     return HttpResponseRedirect(reverse('web:test_redirect'));
#
# # RESPONSE REDIRECT
# def test(request):
#     return HttpResponse("Hello Django Again from test redirect");

from django.shortcuts import render
from web.models import AboutClass, RegistrationClass
from django.http.response import HttpResponse


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


def registration(request):
    if request.method == "POST":
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        _phone = request.POST.get('phone')
        _education = request.POST.get('education')
        _dob = request.POST.get('dob')
        _message = request.POST.get('message')
        RegistrationClass.objects.create(
            name=_name, email=_email, phone=_phone, education=_education, dob=_dob, message=_message
        )
        return HttpResponse("form submitted")
    else:
        return HttpResponse("invalid request!")
