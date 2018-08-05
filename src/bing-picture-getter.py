# Gets the picture of the day in python to the file bing-picture.png

OUTPUT_FILE = "bing-picture.png"
JSON_REQUEST_URL = "http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
IMG_URL_PREPEND = "http://www.bing.com"

import json
import urllib
import urllib.request


def get_image_url(to_prepend, in_request_url):
    # fetch the image json file
    with urllib.request.urlopen(in_request_url) as url:
        data = json.loads(url.read().decode())
        return to_prepend + data['images'][0]['url']


img_url = get_image_url(IMG_URL_PREPEND, JSON_REQUEST_URL)
print("Fetching image {}...".format(img_url))
img_file = open(OUTPUT_FILE, 'wb')
img_file.write(urllib.request.urlopen(img_url).read())
img_file.close()
