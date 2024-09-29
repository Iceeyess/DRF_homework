from re import search

from rest_framework.validators import ValidationError

class VideoLinkValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        search_phrase = 'www.youtube.com'
        if not search_phrase in tmp_val:
            raise ValidationError('Video link is not valid')