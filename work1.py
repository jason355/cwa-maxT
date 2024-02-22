import requests
import tkinter as tk

openweather_api_key = "f78a1322a0d3d098148a0afc21f2de47"
cwa_api_key = "CWA-FCA76849-D9AC-4D9F-BDAF-98A0F4D4FFC6"
city = "Taipei"


root = tk.Tk()
root.geometry("400x300") 
root.title("最高溫預測")
font_style_large = ("新細明體", 14)
label = tk.Label(root, text="請輸入縣市：")
label.pack()


entry = tk.Entry(root)
entry.pack()

def clear_labels():

    for label in root.winfo_children():
        if isinstance(label, tk.Label): 
            label.destroy()


def get_input():
    clear_labels()
    location_Name = entry.get()
    if "台" in location_Name:
        location_Name = "臺"+location_Name[1:] 

    url = f'https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization={cwa_api_key}&format=JSON&locationName={location_Name}&elementName=MaxT'
    try:
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
            root.update_idletasks()
        else:
            print('Failed to retrieve weather data from CWB.')
    except Exception as e:
        text = tk.Label(root, text="請輸入正確的縣市", justify="left", padx=10, pady=5, font=font_style_large, fg="red")
        text.pack(anchor="center")
        root.update_idletasks()



button = tk.Button(root, text="查詢", command=get_input)
button.pack()


root.mainloop()

