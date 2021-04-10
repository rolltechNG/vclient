# Create your views here.
import json

import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from frontend.forms import NINPostForm, PhonePostForm, DemoPostForm


class Home(TemplateView):
    template_name = "hello-world.html"


def post_nin(request):
    if request.method == 'POST':
        form = NINPostForm(request.POST)
        if form.is_valid():
            nin = form.cleaned_data['nin']
            url = request.build_absolute_uri(reverse_lazy('nin_verification',
                                                          kwargs={'token': 14499009348927979530087,
                                                                  'nin': nin},
                                                          ))
            r = requests.get(url=url)
            resp = r.text
            resp_json = json.loads(resp)
            resp_list = resp_json['data']

            return render(request, 'ninsuccess.html', {'response': resp_list})
    else:
        form = NINPostForm()
    context = {'form': form, }

    return render(request, 'ninform.html', context)


def post_phone(request):
    if request.method == 'POST':
        form = PhonePostForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            url = request.build_absolute_uri(reverse_lazy('phone_verification',
                                                          kwargs={'token': 14499009348927979530087,
                                                                  'phone': phone_number},
                                                          ))
            r = requests.get(url=url)
            resp = r.text
            resp_json = json.loads(resp)
            resp_list = resp_json['data']
            print(resp_list)

            return render(request, 'phonesuccess.html', {'response': resp_list})
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
                                                          kwargs={'token': 14499009348927979530087,
                                                                  'firstname': firstname,
                                                                  'lastname': lastname,
                                                                  'dob': dob, }
                                                          ))
            r = requests.get(url=url)
            resp = r.text
            final_resp = json.loads(resp)
            resp_list = final_resp['data']

            return render(request, 'demosuccess.html', {'response': resp_list})
    else:
        form = DemoPostForm()
    context = {'form': form, }

    return render(request, 'demoform.html', context)
