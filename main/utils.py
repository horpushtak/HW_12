import json
from exсeptions import DataJsonError

def load_json_data(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:  # на 40 минуте объяснение рейза ошибки на предмет наличия файла
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise DataJsonError


def search_post_by_substring(posts, substring):
    posts_founded = []  # Никак не уловлю, почему список, возможно для лёгкости перебора, ведь куда ещё складывать?
    for post in posts:
        if substring.lower() in post["content"].lower():
            posts_founded.append(post)
    return posts_founded
