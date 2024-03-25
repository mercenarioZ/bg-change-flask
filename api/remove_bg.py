from gradio_client import Client, file
from PIL import Image
from io import BytesIO


def add_white_bg(image_path):
    # image = Image.open(image_path)
    client = Client("ECCV2022/dis-background-removal")
    result = client.predict(
        file(image_path), api_name="/predict")

    # get the result image
    result_image = Image.open(result[0])

    # add the white background
    result_image = result_image.convert("RGBA")
    white_bg = Image.new("RGBA", result_image.size, (255, 255, 255))
    result_image = Image.alpha_composite(
        white_bg, result_image.convert("RGBA"))
    # bytesIO
    img_io = BytesIO()
    result_image.save(img_io, "PNG")
    img_io.seek(0)

    # save the image
    # result_image.save("output_test.png")

    # return the image file
    return img_io.getvalue()
