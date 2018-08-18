from django.shortcuts import render
from django.views import View
from ete.instagram_scraper import InstagramScraper


class HomeView(View):

    def get(self, request):
        context = {
            'ig_media': InstagramScraper.get_media_links()
        }
        return render(request, 'home/index.html', context=context)
