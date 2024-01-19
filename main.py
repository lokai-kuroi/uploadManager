import eel

# Definiere die Webseitenfunktionen
@eel.expose
def hello_world():
    return "Hallo, Welt!"

# Starte die EEL-App
eel.init('web')
eel.start('index.html', size=(400, 300))
