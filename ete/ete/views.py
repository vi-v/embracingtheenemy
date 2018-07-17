from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception=None, template_name='404.html'):
    return render(request, 'ete/404.html', {}, status=404)
