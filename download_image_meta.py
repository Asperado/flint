#
# Get Image Meta API: 
#  http://www.flickr.com/services/api/flickr.photos.getInfo.html
# 
# Image Format: 
#  http://www.flickr.com/services/api/misc.urls.html
#

from image_parser import *
from image_loader import *
from flickrlib.flickrapi2 import FlickrAPI 
from config import *

class FlickrImageAPI:
    api_key = ''
    api_secret = ''

    def __init__(self):
        self.api_key = keys[0]
        self.api_secret = secrets[0]
        self.flickrAPI = FlickrAPI(self.api_key, self.api_secret)
        
    def get_image_meta(self, image_id):
        print ('Get image meta.')
        data = self.flickrAPI.photos_getinfo(api_key = self.api_key,
                                             photo_id = image_id,
                                             secret = self.api_secret)
        return data
    
    def parse_image_meta(self, parser, data):
        print ('Parse image meta.')
        photo = parser.create_photo(data)
        return photo

if __name__ == '__main__':
    print ('Done get image meta.')
    id_loader = ImageIdLoader()
    image_ids = id_loader.load_image_id()
    
    flickr_api = FlickrImageAPI()
    data = flickr_api.get_image_meta(image_ids[0])
    parser = FlickrImageMetaParser()
    photo = flickr_api.parse_image_meta(parser, data)
    print (photo)
