import json
import datetime


class Post(object):

    def __init__(self):
        self.location = None
        self.photo = None
        self.date = None

    def clean(self):
        self.location = None
        self.photo = None
        self.date = None

    def save(self):
        data = {
            'location': {
                'latitude': self.location.latitude,
                'longitude': self.location.longitude
            },
            'photo': self.photo,
            'date': datetime.datetime.now().strftime("%Y%m%d")
        }

        with open('data.json', 'r') as file:
            file_data = json.load(file)

        file_data['data'].append(data)

        with open('data.json', 'w') as file:
            file.write(json.dumps(file_data))
