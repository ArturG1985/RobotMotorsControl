from machine import Pin

button_l = Pin(18, Pin.IN, Pin.PULL_UP)
button_r = Pin(19, Pin.IN, Pin.PULL_UP)

dr1 = Pin(22, Pin.OUT)
dr2 = Pin(23, Pin.OUT)

press = False
n_pin = 0

def my_button(pin):
    global press
    press = True
    global n_pin
    n_pin = int(str(pin)[4:-1])

button_l.irq(trigger=Pin.IRQ_FALLING, handler=my_button)
button_r.irq(trigger=Pin.IRQ_FALLING, handler=my_button)

while True:
    if press:
        print(n_pin)
        press = False
        
        if n_pin == 18:
            dr1.value(0)
            dr2.value(1)
            print('Вправо')
        elif n_pin == 19:
            dr1.value(1)
            dr2.value(0)
            print('Влево')
        else:
            pass #ничего не делаем


#вносим код с изменениями (например, функции плавного изменения скорости или обработки пользовательского ввода)
#ВНОСИМ ДОПОЛНИТЕЛЬНЫЕ ИЗМЕНЕНИЯ ДЛЯ ПУЛ-РЕКВЕСТА
