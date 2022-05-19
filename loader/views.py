import json
from flask import Blueprint, render_template, request
import logging
from main import utils
from loader.utils import save_uploaded_image, load_post
from config import POST_PATH
from exсeptions import WrongImgType

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post")  # Дефолтный метод GET, (50:00). Если открыть страницу - GET
def create_new_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])  # Если отправить данные - POST
def create_new_post_by_user():
    picture = request.files.get("picture")  # Метод request.files позволяет работать с медиа
    content = request.form.get("content")
    if not picture or not content:  # not None = True
        logging.info("Данные не загружены, часть данных не введена")
        return "Часть данных не введена"

    posts = utils.load_json_data(POST_PATH)
    try:
        new_post = {"pic": save_uploaded_image(picture), "content": content}
    except WrongImgType:
        return "Неверный формат файла"
    load_post(posts, new_post)

    return render_template("post_uploaded.html", new_post=new_post)
