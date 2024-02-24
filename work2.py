import requests
import tkinter as tk

cwa_api_key = "" #填入你的key
location_Name = "臺北市" # 設定地區
url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={cwa_api_key}&format=JSON&locationName={location_Name}&elementName=MaxT'

root = tk.Tk() # 建立視窗
root.geometry("400x300") # 設定視窗大小
root.title("最高溫預測") # 設定標題文字
font_style_large = ("新細明體", 14) # 建立字體樣式 

response = requests.get(url) # 取得data
if response.status_code == 200:
    data = response.json() # 使用json解析資料
    location = data['records']['location']  # 將取得資料範圍縮小至 location部分 ，儲存到變數中
    locationName =  location[0]['locationName'] # 取得地點
    time = location[0]['weatherElement'][0]['time'] # 將資料範圍縮小至time中
    location_label = tk.Label(root, text="地點: "+locationName, justify= "left", padx=10, pady=5, font=font_style_large) #建立標題文字
    location_label.pack(anchor="w") # 設定至父畫面中
    for item in time: # 遍歷所有time中的元素
        startTime = item['startTime'] # 開始時間
        endTime = item['endTime'] # 結束時間
        timeRange = startTime + " 到 " + endTime # 時間字串
        temperature = item['parameter']['parameterName'] # 取得最高氣溫數值
        value = "最高氣溫: " + temperature + "\u00b0C" # 建立氣溫字串

        time_label = tk.Label(root, text=timeRange, justify="left", padx=10, pady=5, font=font_style_large) # 建立時間範圍文字
        value_label = tk.Label(root, text=value, justify="left", padx=10, pady=5, font=font_style_large)  # 建立氣溫文字
        time_label.pack(anchor="w") # 設定至畫面的左方
        value_label.pack(anchor="w")  # 同上
    root.mainloop()

else:
    print('Failed to retrieve weather data from CWB.') # 若失敗則輸出







