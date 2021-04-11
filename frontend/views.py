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
            for key in resp_list:
                img_decode = key['photo']
                signature_decode = key['signature']
                key['photo'] = f"data:image/png;base64,{img_decode}"
                key['signature'] = f"data:image/png;base64,{signature_decode}"
            response = key

            return render(request, 'ninsuccess.html', {'response': response})
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
            for key in resp_list:
                img_decode = key['photo']
                signature_decode = key['signature']
                key['photo'] = f"data:image/png;base64,{img_decode}"
                key['signature'] = f"data:image/png;base64,{signature_decode}"
            response = key

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
                                                          kwargs={'token': 14499009348927979530087,
                                                                  'firstname': firstname,
                                                                  'lastname': lastname,
                                                                  'dob': dob, }
                                                          ))
            r = requests.get(url=url)
            resp = r.text
            resp_json = json.loads(resp)
            resp_list = resp_json['data']
            for key in resp_list:
                img_decode = key['photo']
                signature_decode = key['signature']
                key['photo'] = f"data:image/png;base64,{img_decode}"
                key['signature'] = f"data:image/png;base64,{signature_decode}"
            response = key

            return render(request, 'demosuccess.html', {'response': response})
    else:
        form = DemoPostForm()
    context = {'form': form, }

    return render(request, 'demoform.html', context)
