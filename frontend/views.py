# Create your views here.

import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from frontend.forms import NINPostForm, PhonePostForm, DemoPostForm
from frontend.helpers import process_resp
from verification.models import AccessToken

ACCESS_TOKEN = AccessToken.objects.get(id=1)


class Home(TemplateView):
    template_name = "hello-world.html"


class TestPayment(TemplateView):
    template_name = "test_payment.html"


def post_nin(request):
    if request.method == 'POST':
        form = NINPostForm(request.POST)
        if form.is_valid():
            nin = form.cleaned_data['nin']
            url = request.build_absolute_uri(reverse_lazy("nin_verification",
                                                          kwargs={"token": ACCESS_TOKEN.token,
                                                                  "nin": nin},
                                                          ))
            send_request = requests.get(url=url)
            response = process_resp(send_request)

            return render(request, 'ninsuccess.html', {'response': response})
    else:
        form = NINPostForm()

    context = {'form': form, }
    return render(request, 'ninform.html', context)


def post_phone(request):
    """
    - Interact with api and return json if request is POST
    - Render the form template if request GET
    """
    if request.method == 'POST':
        form = PhonePostForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            # call the phone_verification endpoint in the api app
            url = request.build_absolute_uri(reverse_lazy('phone_verification',
                                                          kwargs={'token': ACCESS_TOKEN.token,
                                                                  'phone': phone_number},
                                                          ))
            r = requests.get(url=url)
            response = process_resp(r)

            return render(request, 'phonesuccess.html', {'response': response})
    else:
        form = PhonePostForm()
    context = {'form': form, }

    return render(request, 'phoneform.html', context)


def post_demo(request):
    if request.method == 'POST':
        form = DemoPostForm(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            dob = form.cleaned_data['dob']
            url = request.build_absolute_uri(reverse_lazy('demo_verification',
                                                          kwargs={'token': ACCESS_TOKEN.token,
                                                                  'firstname': firstname,
                                                                  'lastname': lastname,
                                                                  'dob': dob, }
                                                          ))
            r = requests.get(url=url)
            response = process_resp(r)

            return render(request, 'demosuccess.html', {'response': response})
    else:
        form = DemoPostForm()
    context = {'form': form, }

    return render(request, 'demoform.html', context)
