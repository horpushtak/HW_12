from flask import Blueprint, render_template, request
import logging
from main.utils import load_json_data, search_post_by_substring
from config import POST_PATH
from exсeptions import DataJsonError


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s", "") # пустая строка возвращается, чтобы не было ошибки (15:40)
    logging.info("Выполняется поиск")
    try:
        posts = load_json_data(POST_PATH)
    except DataJsonError:
        return "Невозможно открыть файл с постами"
    founded_posts = search_post_by_substring(posts, s) # Считываем пользовательский ввод
    return render_template("post_list.html", posts=founded_posts, s=s) # (36:30 пометка об уровнях считывания, кто что запускает)