from iconic_application import *
from flickr_api import *

from mapreduce_local import mapper_run

def generate_input_data(app, image_ids_file, image_meta_root):
    import os
    if (not(os.path.exists(image_ids_file))):
        print ('image ids file %s does not exist.' % image_ids_file)
        exit(1)
        
    input = []

    app.load_image_id_from_file(image_ids_file)
    image_ids = app.load_image_id()

    for image_id in image_ids:
        filepath = app.get_image_meta_filepath(image_meta_root, image_id)
        input_entry = {}
        input_entry['image_id'] = image_id
        input_entry['image_path'] = filepath
        input.append(input_entry)

    return input

def generate_image_meta(image_id, meta_output_path):
    import os
    if (os.path.exists(meta_output_path)):
        print ('skip %s' % meta_output_path)
        return

    flickr_api = FlickrImageAPI()
    data = flickr_api.get_image_meta(image_id)
    parser = FlickrImageMetaParser()
    photo = flickr_api.parse_image_meta(parser, data)
    photo_dao = PhotoDao()
    photo_dao.save_meta(photo, meta_output_path)

def generate_image_meta_mapper(input):
    generate_image_meta(input['image_id'], input['image_path'])

def unit_test():
    image_ids_file = './tmp/image_ids.txt'
    app = IconicApplication()
    input = generate_input_data(app, image_ids_file, './tmp/Iconic/data/meta/food')
    generate_image_meta_mapper(input[0])
    
    mapper_run(generate_image_meta_mapper, input)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Flickr Image Meta Downloader')
    parser.add_argument('-i', dest = 'image_ids_file', metavar='i',
                        help='file containing image ids.')
    parser.add_argument('-r', dest = 'image_meta_root', metavar='r',
                        default='./tmp', help='root dir to output meta data.')

    args = parser.parse_args()
    try:
        assert (args.image_ids_file)
        assert (args.image_meta_root)
    except:
        parser.print_help()

    
    image_ids_file = args.image_ids_file
    app = IconicApplication()
    input = generate_input_data(app, image_ids_file, args.image_meta_root)
    generate_image_meta_mapper(input[0])
    
    mapper_run(generate_image_meta_mapper, input)
