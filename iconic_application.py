class IconicApplication:
    def load_image_id_from_file(self, filepath):
        fin = open(filepath, 'r')
        self.load_image_id_from_array(fin)
        fin.close()

    def load_image_id_from_array(self, array):
        self.image_ids_raw = {}
        for line in array:
            line = line.strip()
            lines = line.split('_')
            self.image_ids_raw[lines[1]] = line

    def load_image_id(self):
        image_ids = []
        for line in self.image_ids_raw.keys():
            image_ids.append(line)
        return image_ids

    def get_image_meta_filepath(self, image_meta_root, image_id):
        image_id_raw = self.image_ids_raw[image_id]
        filepath = '/'.join([image_meta_root, image_id_raw[0:5], image_id_raw + '.txt'])
        return filepath


if __name__ == '__main__':
    app = IconicApplication()
    image_id_raw = ['05180076_4342703027']
    image_id = '4342703027'
    app.load_image_id_from_array(image_id_raw)
    meta_filepath = app.get_image_meta_filepath('/nas11/compsci/hongtao/Iconic/data/meta/food', image_id)
    print (meta_filepath)
