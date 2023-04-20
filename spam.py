import pyautogui
# import webbrowser as wb
import time
import pandas as pd
import requests
import numpy as np
# wb.open("web.whatsapp.com")
# position = pyautogui.position()
# pesan = "Aiyoo broo,, ini pesan spam "
time.sleep(5)




url = 'https://raw.githubusercontent.com/skjorrface/animals.txt/master/animals.txt'
response = requests.get(url)
lines = response.text.split('\n')

data = np.array([line.strip().split() for line in lines], dtype=object)
pesan = "Daftar Lahh oii babang bocil "
# print(data[0][0])

for a in range(20):
    #pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    # if len(data[a]) == 3:
    #     pyautogui.typewrite(pesan + data[a][2])
    #     print(pesan + data[a][2])
    # elif len(data[a]) == 2:
    #     pyautogui.typewrite(pesan + data[a][1])
    #     print(pesan + data[a][1])
    # else :
    #     pyautogui.typewrite(pesan + data[a][0])
    #     print(pesan + data[a][0])

    pyautogui.press('enter')
    time.sleep(0.5)




