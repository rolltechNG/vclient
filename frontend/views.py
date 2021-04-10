# Create your views here.
import json

import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from frontend.forms import NINPostForm


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
            final_resp = json.loads(resp)
            resp_list = final_resp['data']

            return render(request, 'ninsuccess.html', {'resp': resp_list})
    else:
        form = NINPostForm()
    context = {'form': form, }

    return render(request, 'ninform.html', context)
