from instalooter.looters import ProfileLooter


class InstagramScraper:
    num_hits = 0
    cache = None
    
    @staticmethod
    def get_media_links():
        InstagramScraper.num_hits += 1
        if InstagramScraper.num_hits % 20 == 1:
            InstagramScraper.num_hits = 0
        else:
            return InstagramScraper.cache

        looter = ProfileLooter('embracingtheenemy')
        InstagramScraper.cache = [{
            'src': media['thumbnail_src'],
            'is_video': media['is_video'],
            'shortcode': media['shortcode']
        } for media in looter.medias()][:3]
        return InstagramScraper.cache
