from config import UPLOAD_FOLDER, POST_PATH
from exсeptions import WrongImgType
import json


def save_uploaded_image(picture):
    allowed_type = ["jpg", "jpeg", "png", "gif"]
    picture_type = picture.filename.split('.')[-1]
    if picture_type not in allowed_type:
        raise WrongImgType(f"Неправильный формат файла. Допустимые форматы: {(', ').join(allowed_type)}")

    picture_path = (f"{UPLOAD_FOLDER}/{picture.filename}")  # ???????
    picture.save(picture_path)  # ????????

    return picture_path


def load_post(posts_list, new_post):
    posts_list.append(new_post)  # Добавляем к списку новый пост
    with open(POST_PATH, "w", encoding="utf-8") as file:
        # Записываем обновлённый список в posts.json стирая старую инфу и целиком
        # запихивая новую
        json.dump(posts_list, file)
