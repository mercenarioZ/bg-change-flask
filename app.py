from flask import Flask, request, send_file, render_template
from io import BytesIO
import subprocess
from PIL import Image
from rembg import remove

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def image_process():
    if request.method == "POST":
        if "image_file" not in request.files:
            return "No file uploaded", 400
        image_file = request.files["image_file"]
        if image_file.filename == "":
            return "No file selected", 400
        if image_file:
            input_image = Image.open(image_file.stream)
            output_image = remove(input_image)
            img_io = BytesIO()
            output_image.save(img_io, 'PNG')
            img_io.seek(0)
            return send_file(img_io, mimetype='image/png', as_attachment=True, download_name='bg-removed.png')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
