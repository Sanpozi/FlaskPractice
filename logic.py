
import csv
import datetime
import os
import matplotlib
matplotlib.use('Agg') # バックエンドで動作？
import matplotlib.pyplot as plt

current_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_path)

def readcsv():
    csv_data = []
    with open('./data/number.csv', newline='') as csvfile:
        sparamreader = csv.reader(csvfile)
        for row in sparamreader:
            print(row)
            csv_data.append(row)
    return csv_data

def appendcsv(dict):
    if datacheck(dict):
        with open('./data/number.csv','a') as csvfile:
            writer = csv.DictWriter(csvfile, ['Date', 'Cash', 'UFJ', 'RakutenBank', 'RakutenShoken'])
            writer.writerow(dict)
    else:
        raise Exception("入力データが不正です")

def create_png():
    csv_data = readcsv()
    
    date = []
    cash = []
    ufj = []
    rakuten_b = []
    rakuten_s = []
    cre_t = []
    cre_n = []

    for row in csv_data[1:]:
        date.append(datetime.datetime.strptime(row[0], '%Y-%m-%d'))    
        cash.append(int(row[1]))
        ufj.append(int(row[2]))
        rakuten_b.append(int(row[3]))
        rakuten_s.append(int(row[4]))

    mylabels =['cash', 'ufj', 'rakuten_bank', 'rakuten_shoken']

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    # 積み上げ面グラフ
    ax.stackplot(date, cash, ufj, rakuten_b, rakuten_s, labels=mylabels)
    ax.legend(loc='upper left')
    # 目盛の設定
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%y-%m'))
    ax.yaxis.get_major_formatter().set_scientific(False)
    ax.grid(which = "major", axis = "y", color = "grey", alpha = 0.8,
        linestyle = "--", linewidth = 1)
    #plt.show()
    fig.savefig("data/figure.png")

def datacheck(data):
    try:
        datetime.datetime.strptime(data['Date'],"%Y-%m-%d")
        int(data['Cash']) 
        int(data['UFJ']) 
        int(data['RakutenBank']) 
        int(data['RakutenShoken'])
        return True
    except ValueError:
        return False


# デバッグ用
# create_png()