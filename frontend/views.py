# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView

from frontend.forms import NINPostForm


class Home(TemplateView):
    template_name = "hello-world.html"


def post_nin(request):
    form = NINPostForm()
    return render(request,
                  'ninform.html',
                  {'form': form}
                  )
