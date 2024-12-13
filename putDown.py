#pyinstaller --onefile --icon="putDown.ico" putDown.py

from pynput import keyboard
from pynput.keyboard import Controller
import threading
import time

keyboard_controller = Controller()
    
c_key_pressed = False
stop_thread = False
thread = None

def press_c_key():
    """'c' 키를 계속 누르는 스레드."""
    global stop_thread
    if not stop_thread:
        keyboard_controller.release('c')
        keyboard_controller.press('c')

def on_press(key):
    global c_key_pressed, stop_thread, thread
    try:
        if key.char == 'l':
            if not c_key_pressed:
                print("매크로를 시작합니다.")
                c_key_pressed = True
                stop_thread = False
                thread = threading.Thread(target=press_c_key)
                thread.start()
            else:
                print("매크로를 종료합니다.")
                keyboard_controller.release('c')
                c_key_pressed = False
                stop_thread = True
                if thread:
                    thread.join()
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
    # if key.char == ';':
        print("프로그램을 종료합니다.")
        return False

print("게임이 시작되면 L키를 누르세요.")
print("프로그램을 종료하려면 ;키를 누르세요.")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()