import pyautogui as pag
import time
import keyboard
from PIL import ImageGrab


def job():
    icons = list(pag.locateAllOnScreen('a.png'))
    if len(icons) == 0:
        icons = list(pag.locateAllOnScreen('aa.png'))
    #e5efe7
    #e9f3eb
    print("ABIBA")
    for icon in icons:
        print(icon)
        pag.click(icon.left + icon.width/2, icon.top + icon.height/2)
        # pag.click(icon)

        stat = pag.locateOnScreen('stat.png')
        pag.moveTo(stat.left + stat.width/2, stat.top + stat.height/2)

        target_color = (233, 243, 235)
        screenshot = ImageGrab.grab()
        width, height = screenshot.size
        leave = False
        for x in range(width):
            for y in range(height):
                pixel = screenshot.getpixel((x, y))
                if pixel == target_color:
                    pag.click(x, y)
                    leave = True
                    break
                if leave == True:
                    break
    
    next_button = pag.locateOnScreen('next.png')
    if next_button:
        pag.click(next_button.left + next_button.width/2, next_button.top + next_button.height/2)
    
    end_button = pag.locateOnScreen('next.png')
    if end_button:
        pag.click(end_button.left + end_button.width/2, end_button.top + end_button.height/2)


can_press = True
if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            break
        if keyboard.is_pressed('r') and can_press:
            job()
            can_press = False
        elif not keyboard.is_pressed('r'):
            can_press = True

