# 程式開頭會import需要用到的package
import pymysql
# 這裡用到的是pymysql這個package
# 若沒安裝過的package要在終端機安裝
# 以安裝pymysql這個package為例，在終端機輸入: pip install pymysql
# (若為macOS輸入: pip3 install pymysql)

# 資料庫參數設定
db_settings = {
    #host為連接的伺服器位置，我們連接本地端
    #可輸入"127.0.0.1"或"loaclhost"
    "host": "127.0.0.1",
    #port為接口，預設3306
    "port": 3306,
    #使用者
    "user": "root",
    #密碼
    "password": "cycucycu",
    #資料庫名稱
    "db": "test1",
    #編碼方式
    "charset": "utf8"
}

try:
    # 建立Connection物件
    conn = pymysql.connect(**db_settings)

    #儲存
    conn.commit()
except Exception as ex:
    #若try:區域內有問題會在此印出錯誤
    print(ex)

