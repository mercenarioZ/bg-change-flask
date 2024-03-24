from flask import Flask, request, send_file, render_template, render_template_string
from script import remove_background
from io import BytesIO
from werkzeug.utils import secure_filename

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
            # get the extension of the file
            filename = secure_filename(image_file.filename)
            file_extension = filename.rsplit(
                '.', 1)[1].lower() if '.' in filename else ''

            allowed_extensions = {'jpg', 'jpeg', 'png'}
            # check if the file is allowed
            if file_extension not in allowed_extensions:
                return render_template_string('''
                    <h1>Invalid file extension</h1>
                    <p>Only .jpg, .jpeg, .png files are allowed</p>
                    <a href="/">Go back</a>
                '''), 400

            try:
                processed_img = remove_background(image_file)
                return send_file(BytesIO(processed_img), mimetype="image/png", as_attachment=True, download_name="processed_image.png")
            except Exception as e:
                return str(e), 500
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5433)
