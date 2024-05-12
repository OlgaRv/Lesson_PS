import requests

img ="https://img.freepik.com/premium-photo/colorful-flower-wallpapers-hd-wallpapers_802639-6371.jpg?w=1380"

response = requests.get(img)
with open("test.jpg", "wb") as f:
    f.write(response.content)