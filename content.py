import requests


class Content:
    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def get_content(self):
        # make a request
        url = f'https://api.nasa.gov/planetary/apod?api_key={self.api_key}'
        response = requests.get(url).json()

        title = response['title']
        text = response['explanation']
        image_url = response['url']
        # get image
        response_image = requests.get(image_url)
        with open('image.jpg', 'wb') as file:
            file.write(response_image.content)
        return [title, text]




