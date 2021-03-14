# FlaskPractice
資産の推移をmatplotlibで描画してFlask上で表示させる。
データはcsvで管理。

## Deploy

リポジトリをプル後、

~~~terminal
cd {project path}
mkdir data
touch data/number.csv
pip install -r requirements.txt
python3 main.py
(ssh接続時などサーバ上のバックグラウンドで実行したい場合は以下)
nohup python3 main.py 2>&1 
~~~

サーバの5000ポートにデプロイされます。
