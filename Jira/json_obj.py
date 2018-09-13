class Json:
    def __init__(self, json_name):
        self.json_name = json_name

    def read_json(self):
        return open('json/' + self.json_name, 'rb')

