from rembg import remove
from PIL import Image


def remove_background(image_path):
    # Load image
    img = Image.open(image_path)
    img = img.convert("RGBA")  # Convert image to RGBA mode

    # Remove background
    processed_img = remove(img, post_process_mask=True)

    # Add the white background to the image
    white_bg = Image.new("RGBA", processed_img.size, (255, 255, 255))
    with_white_background = Image.alpha_composite(
        white_bg, processed_img.convert("RGBA"))

    # Save processed image to a file
    # processed_img.save('./processed_image.png')

    # Save image with white background to a file
    with_white_background.save('./img.png')

    # _, axes = plt.subplots(1, 2, figsize=(10, 5))
    # axes[0].imshow(img)
    # axes[0].set_title('Original Image')
    # axes[0].axis('off')

    # axes[1].imshow(processed_img)
    # axes[1].set_title('Background Removed')
    # axes[1].axis('off')

    # plt.show()


if __name__ == "__main__":
    image_path = './pre-grape.jpg'
    remove_background(image_path)
