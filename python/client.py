#!/usr/bin/env python
import gzip
import json
import io

import requests

URL = 'http://127.0.0.1:9000/'
# URL = 'http://127.0.0.1:9000/alt/'
# URL = 'http://127.0.0.1:9000/drf/'

DATA = {
    # from https://en.wikipedia.org/wiki/JSON
    "firstName": "John",
    "lastName": "Smith",
    "isAlive": True,
    "age": 25,
    "address": {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    },
    "phoneNumbers": [
        {
            "type": "home",
            "number": "212 555-1234"
        },
        {
            "type": "office",
            "number": "646 555-4567"
        },
        {
            "type": "mobile",
            "number": "123 456-7890"
        }
    ],
    "children": [],
    "spouse": None,
}


def upload_plain_json():
    response = requests.post(URL, json=DATA)

    print('Response to plain upload:\n{}\n'.format(response.text))


def upload_gzip_json():
    gz_buffer = io.BytesIO()
    gz_file = gzip.GzipFile(mode='wb', fileobj=gz_buffer)
    gz_file.write(json.dumps(DATA))
    gz_file.close()
    gz_data = gz_buffer.getvalue()

    response = requests.post(URL,
                             data=gz_data,
                             headers={
                                 'content-type': 'application/json',
                                 'content-encoding': 'gzip',
                             })

    print('Response to gzip upload:\n{}\n'.format(response.text))


def main():
    upload_plain_json()
    upload_gzip_json()


if __name__ == '__main__':
    main()
