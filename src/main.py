from flask import Flask, render_template, request

from .config import get_settings
from .summerize import summarize

settings = get_settings()


app = Flask(
    __name__,
    static_folder=settings.STATIC_DIR,
    static_url_path=settings.STATIC_URL,
    template_folder=settings.TEMPLATES_DIR,
)
app.debug = settings.DEBUG
app.secret_key = settings.SECRET_KEY
app.config["TEMPLATES_AUTO_RELOAD"] = bool(1)
app.config["ENV"] = "development"
app.config["DEBUG"] = settings.DEBUG


@app.route("/", methods=["GET", "POST"])
def index():
    content = new_value = None
    is_danger_alert = is_success_alert = False
    if request.method == "POST":
        content = request.form.get("content")
        words = len(content.split())
        if content != "" and words >= 100:
            val = summarize(content)
            new_value = val
            is_danger_alert = False
            is_success_alert = True
        else:
            is_danger_alert = True
            is_success_alert = False
    return render_template(
        "index.html",
        data=new_value,
        content=content,
        is_danger_alert=is_danger_alert,
        is_success_alert=is_success_alert,
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404
