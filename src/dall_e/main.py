import os

import requests
from openai import OpenAI
from dotenv import load_dotenv


def main():
    load_dotenv()
    print(f"Using OpenAI API key {os.environ['OPENAI_API_KEY_NAME']}")

    client = OpenAI()

    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )

    print(f"Rendered image: {response.data[0].url}")

    image_data = requests.get(response.data[0].url).content
    with open("output.jpg", "wb") as file:
        file.write(image_data)


if __name__ == "__main__":
    main()
