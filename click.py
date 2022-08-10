from time import sleep
import pyautogui
import keyboard


# pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True


priceData = []
nameData = []

def downloadData():
    with open("price.txt", "r") as price:
        for data in price:
            priceData.append(data.strip())
    with open("name.txt", "r") as name:
        for data in name:
            nameData.append(data.strip())

def firtPosition():
    pyautogui.moveTo(900, 177)

def click(count):
    if count == 1:
        pyautogui.click()
    if count == 2:
        pyautogui.doubleClick()
    if count == 3:
        pyautogui.tripleClick()

def writeNameData(i):
    pyautogui.write(nameData[i])
    pyautogui.press('enter')

def pricePosition():
    pyautogui.moveTo(1060,244)
    click(1)
    sleep(1)
    pyautogui.moveTo(1111, 246)
    click(3)

def writePriceData(i):
    pyautogui.write(priceData[i])
    pyautogui.press('enter')




print('Привет, укажи с какого товара начать')
start = int(input()) - 1

print('\n')

sleep(1)

print('Загрузка данных...')
downloadData()
print('Загружено!')
print('\n')

print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('\n')



for i in range(start, len(nameData)):
    if keyboard.is_pressed('esc'):  # if key 'esc' is pressed 
        print('Stop!')
        break  # finishing the loop
    print(i + 1, nameData[i], priceData[i])
    firtPosition()
    click(3)
    writeNameData(i)
    sleep(1)
    pricePosition()
    writePriceData(i)
    sleep(1) 
    # keyboard.wait('esc') # ждем эскейпа

       
            
print('end')