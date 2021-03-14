# FlaskPractice
資産の推移をmatplotlibで描画してFlask上で表示させる。
データはcsvで管理。

## Deploy
~~~terminal
python3 -m venv {venvpath}
source {venvpath}/bin/activate
pip install requirements.txt
deactivate
~~~

.pyファイルを仮想環境下に配置後、

~~~terminal
source {venvpath}/bin/activate
python main.py
~~~

サーバの5000ポートにデプロイされます。
