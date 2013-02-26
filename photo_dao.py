class PhotoDao:
    def save_meta(self, photo, filepath, mapped_key = {}):
        print ('save photo meta to file.')
        import os
        dirname = os.path.dirname(filepath)
        if (not(os.path.exists(dirname))):
            os.makedirs(dirname)

        fout = open(filepath, 'w')
        for key in photo.keys():
            key_name = key
            if (key_name in mapped_key):
                key_name = mapped_key[key_name]
            fout.write(key_name + ':' + photo[key] + '\n')
        fout.close()

    def load_meta(self, filepath, rev_mapped_key = {}):
        fin = open(filepath, 'r')
        photo = {}
        for line in fin:
            data = line.split(':', 1)
            key_name = data[0].strip()
            value = data[1].strip()
            if (key_name in rev_mapped_key):
                key_name = rev_mapped_key[key_name]
            photo[key_name] = value
        fin.close()
        return photo

if __name__ == "__main__":
    photo = {'url_small': 'http://farm2.staticflickr.com/1127/1088952486_393e5208d9_q.jpg', 'datetaken': '2007-08-08', 'server': '1127', 'secret': '393e5208d9', 'url_thumbnail': 'http://farm2.staticflickr.com/1127/1088952486_393e5208d9_t.jpg', 'photo_page': 'http://www.flickr.com/photos/cropwithanna/1088952486/', 'url': 'http://farm2.staticflickr.com/1127/1088952486_393e5208d9_o.jpg', 'url_tiny': 'http://farm2.staticflickr.com/1127/1088952486_393e5208d9_s.jpg', 'owner_location': 'San Diego, USA', 'owner': '74181952@N00', 'tags': 'creativememories,annamona,scrapbooks,sandiego,craftroom,workshoproom,scrapbookroom,cropspace,creativememoriesconsultant,homesweethome,scrapbooking,rubberstamping,photos,sewing', 'id': '1088952486', 'tags_raw': 'Creative Memories,Anna Mona,Scrapbooks,San Diego,Craft room,Workshop room,Scrapbook room,Crop Space,Creative Memories Consultant,Home Sweet Home,Scrapbooking,Rubber Stamping,photos,sewing', 'timetaken': '19:21:59', 'farm': '2'}
    photo_filepath = 'tmp/test_photo.txt'
    photo_dao = PhotoDao()
    photo_dao.save_meta(photo, photo_filepath, {'id':'ID'})
    print (photo_dao.load_meta(photo_filepath, {'ID':'id'}))
