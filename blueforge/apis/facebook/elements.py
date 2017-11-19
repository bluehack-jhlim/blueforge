class Element(object):
    def __init__(self, title, item_url=None,
                 image_url=None, subtitle=None, buttons=None):
        self.title = title
        self.item_url = item_url
        self.image_url = image_url
        self.subtitle = subtitle
        self.buttons = buttons

    def get_data(self):
        data = {
            'title': self.title,
            'item_url': self.item_url,
            'image_url': self.image_url,
            'subtitle': self.subtitle
        }
        if self.subtitle:
            if len(self.subtitle) > 80:
                raise ValueError('The Sub-title variable exceeds the maximum of 80 characters.')

        if self.title:
            if len(self.title) > 80:
                raise ValueError('The Title variable exceeds the maximum of 80 characters.')

        if len(self.buttons) > 3:
            raise ValueError('The Button\' element exceeds the maximum of 3.')

        if self.buttons:
            data['buttons'] = [
                button.get_data() for button in self.buttons
            ]
        return data
