from django.shortcuts import render
from django.views import View
from bio.models import BioContent


class BioView(View):

    def get(self, request):
        bio_content = []
        for content_object in BioContent.objects.all():
            bio_content.append(content_object.content)

        return render(request, 'bio/index.html', context={'content_paragraphs': bio_content})
