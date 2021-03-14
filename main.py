#! python
# -*- encoding: utf-8 -*-
from flask import *
import logic



app = Flask(__name__, static_folder='data')
# 画像の更新を反映させる
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

@app.route('/', methods=['GET','POST'])
def hello():
    try:
        message = 'ようこそ！！'
        if request.method == 'POST':
            data = {}
            data['Date'] =request.form['date']
            data['Cash'] = request.form['cash']
            data['UFJ'] = request.form['ufj']
            data['RakutenBank'] = request.form['rakuten_b']
            data['RakutenShoken'] = request.form['rakuten_s']
            logic.appendcsv(data)
            message = '登録できました！'
        logic.create_png()
    except Exception as e:
        message = e.args
    return render_template('mainpage.html', message = message)


# クライアントにキャッシュさせない
@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "-1"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')