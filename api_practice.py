# コンソールに郵便番号打つと郵便番号を検索するAPIモジュール
import json
import requests

# エンドポイント
url = "https://zipcloud.ibsnet.co.jp/api/search"

# ?params=以降の郵便番号を入力させる（スペースとハイフンは置換）
zipcode = input("郵便番号入力 → ").replace(" ", "")

# requests.get する際のzipcodeをdictに詰める（標準入力したもの）
params = {"zipcode": zipcode }

# ?以降 のクエリストリングをparams= で指定する
res = requests.get(url, params=params)

# JSON形式の文字列を辞書に変換する
values = json.loads(res.text)

# 最終的にクエリストリングをつなげたURLを表示
print(res.url)

# 下記jsonデータの内 address1からaddres３を出力、なければないと伝える
try:
    print(values["results"][0]["address1"] + values["results"][0]["address2"] + values["results"][0]["address3"])
except TypeError as e :
    print("入力された郵便番号はありません")

# ↓
# "results": [
#                 {
#                         "address1": "埼玉県",
#                         "address2": "さいたま市岩槻区",
#                         "address3": "西町",
#                         "kana1": "ｻｲﾀﾏｹﾝ",
#                         "kana2": "ｻｲﾀﾏｼｲﾜﾂｷｸ",
#                         "kana3": "ﾆｼﾏﾁ",
#                         "prefcode": "11",
#                         "zipcode": "3390067"
#                 }
#         ],
