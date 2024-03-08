#Speaker_used_for_windows
import win32com.client as wincl
import time

print(">>What you want me to speak\n>type 'quit()' to exit")
while True:
    sentence = input("")
    time.sleep(2)
    if (sentence == "quit()"):
        speaker = wincl.Dispatch("SAPI.SpVoice")
        message = "Thank you for using this program"
        speaker.Speak(message)
        break
    else:
        speaker = wincl.Dispatch("SAPI.SpVoice")
        message = f"{sentence}"
        speaker.Speak(message)
