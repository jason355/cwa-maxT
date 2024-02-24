import requests
import tkinter as tk

cwa_api_key = "" #填入你的key
location_Name = "臺北市" # 設定地區
url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={cwa_api_key}&format=JSON&locationName={location_Name}&elementName=MaxT'

root = tk.Tk() # 建立視窗
root.geometry("400x300") # 
root.title("最高溫預測")
font_style_large = ("新細明體", 14)

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    location = data['records']['location']
    locationName =  location[0]['locationName']
    time = location[0]['weatherElement'][0]['time']
    location_label = tk.Label(root, text="地點: "+locationName, justify= "left", padx=10, pady=5, font=font_style_large)
    location_label.pack(anchor="w")
    for item in time:
        startTime = item['startTime']
        endTime = item['endTime']
        timeRange = startTime + " 到 " + endTime
        value = "最高氣溫: " + item['parameter']['parameterName'] + "\u00b0C"

        time_label = tk.Label(root, text=timeRange, justify="left", padx=10, pady=5, font=font_style_large)
        value_label = tk.Label(root, text=value, justify="left", padx=10, pady=5, font=font_style_large)
        time_label.pack(anchor="w")
        value_label.pack(anchor="w") 
    root.mainloop()

else:
    print('Failed to retrieve weather data from CWB.')







