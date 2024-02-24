import requests
import tkinter as tk


cwa_api_key = "" # 在這裡填入你的key


# UI 設定
root = tk.Tk() # 建立UI視窗
root.geometry("400x300")  # 設定視窗大小
root.title("最高溫預測") # 設定視窗標題
font_style_large = ("新細明體", 14) # 建立字型
label = tk.Label(root, text="請輸入縣市：") # 設定文字
label.pack() # 將文字放入到視窗中


entry = tk.Entry(root) # 建立輸入框
entry.pack() # 將輸入框放入至視窗中



# 清除畫面中的 label
def clear_labels():
    for label in root.winfo_children():
        if isinstance(label, tk.Label): 
            label.destroy()

# 按下查詢後的函數
def get_input():
    clear_labels() # 先將畫面清空
    location_Name = entry.get() # 取得輸入文字
    if "台" in location_Name: # 若輸入"台"，將其轉換為 "臺" 因"台"會搜尋不到
        location_Name = "臺"+location_Name[1:] 
    # 訪問網址 "{}"中是變數
    url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={cwa_api_key}&format=JSON&locationName={location_Name}&elementName=MaxT'
    try: 
        response = requests.get(url) # 取得資料
        if response.status_code == 200: # 判斷是否成功
            data = response.json() # 將資料使用json格式轉換
            location = data['records']['location'] # 將取得資料範圍縮小至 location 部分，儲存在變數location中
            locationName =  location[0]['locationName'] # 取得地點
            time = location[0]['weatherElement'][0]['time'] # 將資料範圍縮小至time，以便後續取得氣溫
            location_label = tk.Label(root, text="地點: "+locationName, justify= "left", padx=10, pady=5, font=font_style_large) # 設定文字, text 為顯示文字的設定, justify 是對齊的設定, padx pady 為邊寬設定, font 為字體樣式設定，這裡使用剛剛建立好的font_style_large
            location_label.pack(anchor="w") # 設定location_label至視窗左邊，
            for item in time: # 再來使用for 遍歷每個time中的dictionary, 每一次 item都會是一個dictionary
                startTime = item['startTime'] # 取得開始時間
                endTime = item['endTime'] # 取得結束時間
                timeRange = startTime + " 到 " + endTime # 建立時間字串 方便顯示
                temperature = item['parameter']['parameterName'] # 取得最高氣溫數值
                value = "最高氣溫: " + temperature + "\u00b0C" # 建立氣溫字串


                time_label = tk.Label(root, text=timeRange, justify="left", padx=10, pady=5, font=font_style_large) # 建立時間範圍文字
                value_label = tk.Label(root, text=value, justify="left", padx=10, pady=5, font=font_style_large)# 建立氣溫文字
                time_label.pack(anchor="w") # 將文字設定至畫面左側上
                value_label.pack(anchor="w")  # 將文字設定至畫面左側上
            root.update_idletasks() # 更新畫面
        else: 
            print('Failed to retrieve weather data from CWB.') # 若取得資料失敗則輸出在終端機
    except Exception as e: # 錯誤處理 若輸入網址無法取得天氣資料則會跳到至此
        text = tk.Label(root, text="請輸入正確的縣市", justify="left", padx=10, pady=5, font=font_style_large, fg="red")
        text.pack(anchor="center")
        root.update_idletasks()

button = tk.Button(root, text="查詢", command=get_input) # 建立查詢按鈕 command 設定點擊後的函數
button.pack() # 設定至畫面上

root.mainloop() # 執行畫面

