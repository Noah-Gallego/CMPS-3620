from microbit import *
import radio

def setup(channel=7):
    """Setup Radio"""
    radio.on()
    radio.config(channel=channel)

def send_message(message):
    channel = 2
    setup(channel=channel)
    radio.send(message)

def test_channels():
    for i in range(0, 84):
        setup(channel=i)
        print('Testing Channel:', i)
        display.show(i)
        
        start_time = running_time()
        message = None
        
        while running_time() - start_time < 500:
            message = radio.receive()
            if message is not None:
                print("Received:", message)
                return i, message
            sleep(50)
    
    return None, None

channel, message = test_channels()

if channel is not None:
    display.scroll(str(message))
    print('Channel Found:', channel)
    print('Message:', message)
else:
    display.show('X')
    print('No message found on any channel')

if button_a.was_pressed():
    while True:
        # Sherek Image
        send_message('https://tinyurl.com/t8mba7zr')