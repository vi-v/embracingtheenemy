from django.shortcuts import render
from django.views import View
from contact.models import ContactContent
from ete.instagram_scraper import InstagramScraper

class ContactView(View):

    def get(self, request):
        content = []
        for content_object in ContactContent.objects.all():
            content.append(content_object.content)

        context = {
            'content_paragraphs': content,
            'ig_media': InstagramScraper.get_media_links()
        }

        return render(request, 'contact/index.html', context=context)
