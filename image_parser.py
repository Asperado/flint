class FlickrImageMetaParser:
    def __init__(self):
        self.photo_types = {'tiny' : 's', 'small' : 'q', 'thumbnail' : 't', 'original' : 'o'}
        
    def create_photo(self, data):
        print ('create photo');
        photo = {}
        photo['secret'] = data.photo[0]['secret']
        photo['id'] = data.photo[0]['id']
        photo['owner'] = data.photo[0].owner[0]['nsid']
        photo['owner_location'] = data.photo[0].owner[0]['location']
        photo['farm'] = data.photo[0]['farm']
        photo['server'] = data.photo[0]['server']
        photo['url_small'] = self.get_url(photo, 'small')
        photo['url_tiny'] = self.get_url(photo, 'tiny')
        photo['url_thumbnail'] = self.get_url(photo, 'thumbnail')
        photo['url'] = self.get_url(photo, 'original')
        photo['datetaken'] = data.photo[0].dates[0]['taken'].split(' ')[0]
        photo['timetaken'] = data.photo[0].dates[0]['taken'].split(' ')[1]
        photo['photo_page'] = data.photo[0].urls[0].url[0].elementText
        photo.update(self.get_tags(data))
        return photo
        
    def get_tags(self, data):
        raw_tags_data = data.photo[0].tags[0].tag
        raw_tags = []
        tags = []
        for raw_tag_data in raw_tags_data:
            raw_tags.append(raw_tag_data['raw'])
            tags.append(raw_tag_data.elementText)
        result = {}
        result ['tags_raw'] = ','.join(raw_tags)
        result ['tags'] = ','.join(tags)
        return result

    def get_url(self, photo, photo_type):
        url = 'http://farm%s.staticflickr.com/%s/%s_%s_%s.jpg' % (photo['farm'], photo['server'], photo['id'], photo['secret'], self.photo_types[photo_type])
        return url

