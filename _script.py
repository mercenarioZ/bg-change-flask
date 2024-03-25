from rembg import remove
from PIL import Image
from io import BytesIO


def remove_background(image_file):
    # Load image
    img = Image.open(image_file.stream)
    img = img.convert("RGBA")  # Convert image to RGBA mode

    # Remove background
    processed_img = remove(img, post_process_mask=True)

    # Add the white background to the image
    white_bg = Image.new("RGBA", processed_img.size, (255, 255, 255))
    with_white_background = Image.alpha_composite(
        white_bg, processed_img.convert("RGBA"))
    img_io = BytesIO()
    with_white_background.save(img_io, "PNG")
    img_io.seek(0)

    # return the image file
    return img_io.getvalue()
