from flask import Blueprint, render_template, request, redirect
from flask_login import login_user, logout_user, login_required, current_user
from flask_app import db
from flask_app.models import Food
from google.cloud import vision
import os
import re
from dotenv import load_dotenv

receipt_bp = Blueprint('receipt', __name__, url_prefix='/receipt')
load_dotenv() # 環境変数の読み込み


# レシート登録画面
@receipt_bp.route("/", methods=["GET", "POST"])
@login_required
def receipt():
    return render_template('receipt.html')


# OCR結果画面
@receipt_bp.route("/list", methods=["GET", "POST"])
@login_required
def receipt_list():
    if request.method == 'POST':
        file = request.files['receipt-file']

        #JSONファイルの指定
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        
        #APIの実行
        client = vision.ImageAnnotatorClient()
        content = file.read()
        image = vision.Image(content=content)
        response =  client.document_text_detection(
                        image=image,
                        image_context={'language_hints': ['ja']}
                    )
        text= response.text_annotations[0].description
        text_list = text.split() # 抽出したテキストリストの取得

        # 日本語が含まれていないものを除去
        def contains_japanese(text):
            return re.search(r'[ぁ-んァ-ン一-龥]+', text)
        text_list_no_jp = [item for item in text_list if contains_japanese(item)]

        # 以下の単語が含まれている+日付,x個,x点の形式を除去
        words_to_remove = [
            "領収書", "領収証", "営業時間", "年中無休", "レジ", "電話", "商品", "買上", "税",
            "値引", "小計", "合計", "預り", "預かり", "お釣り", "支払", "ポイント", "クレジット", "控え"
        ]
        text_list_removed = [
            item for item in text_list_no_jp if not any(word in item for word in words_to_remove)
            and
            not re.match(r'(\d{4}年\d{1,2}月\d{1,2}日)|(\d{1,2}月\d{1,2}日)|(\d{1,2}個)|(\d{1,2}点)', item)
        ]
        
        return render_template('receipt-list.html', text_list_removed=text_list_removed)
    else:
        return redirect("/food-list")
    

# レシート登録の実行
@receipt_bp.route("/exe", methods=["GET", "POST"])
@login_required
def receipt_exe():
    if request.method == 'POST':
        checked_id_list = request.form.getlist('checkbox')
        for x in checked_id_list:
            user_id = current_user.id
            receipt_food_name = request.form.get("food-name-" + x)
            receipt_limit_date = request.form.get("limit-date-" + x)

            receipt_list = Food(user_id=user_id, food_name=receipt_food_name, limit_date=receipt_limit_date)
            db.session.add(receipt_list)
        db.session.commit()

    return redirect("/food-list")