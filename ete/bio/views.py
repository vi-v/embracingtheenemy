from django.shortcuts import render
from django.views import View
from bio.models import BioContent
from ete.instagram_scraper import InstagramScraper


class BioView(View):

    def get(self, request):
        bio_content = []
        for content_object in BioContent.objects.all():
            bio_content.append(content_object.content)

        context = {
            'content_paragraphs': bio_content,
            'ig_media': InstagramScraper.get_media_links()
        }

        return render(request, 'bio/index.html', context=context)
