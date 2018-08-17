from django.shortcuts import render
from django.views import View
from contact.models import ContactContent


class ContactView(View):

    def get(self, request):
        content = []
        for content_object in ContactContent.objects.all():
            content.append(content_object.content)

        return render(request, 'contact/index.html', context={'content_paragraphs': content})
