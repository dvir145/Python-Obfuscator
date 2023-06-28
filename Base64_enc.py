import base64


def base64_encode(data):
    encoded_data = base64.b64encode(data)
    return encoded_data


class Encoder:
    def __init__(self):
        self.code = ""
        self.enc = ""

    def encode(self, file):
        with open(file, 'rb') as f:
            self.code = f.read()
        encoded = base64_encode(self.code)
        self.enc = f"import base64;exec(base64.b64decode({encoded}));"
