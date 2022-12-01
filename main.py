

# Import Libraries
import tkinter
import customtkinter
from gtts import gTTS
from playsound import playsound


# GUI
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("400x200")
app.title("Roll Call")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, text='By navgup@stanford.edu', justify=tkinter.LEFT)
label_1.pack(pady=10, padx=10)

entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="Type name here:")
entry_1.pack(pady=10, padx=10)


# Functions
def get_language(name):
    '''
    Finds the name in the name reference list; changes TTS language accordingly to get a more accurate pronunciation
    '''
    f = open('names.txt')
    readline = f.readlines()
    lines = readline
    language = 'en'
    if f"{name}\n" in lines:
        i = lines.index(f"{name}\n")
        if i < 501:
            language = 'hi'
        elif i < 922:
            language = 'fr'
        elif i < 1107:
            language = 'es'
        elif i < 1452:
            language = 'ru'
        else:
            language = 'en'
    return language


def tts():
    '''
    Given a name and a language, outputs the name audio
    '''
    name = entry_1.get()
    name = name.lower()
    tts_lang = get_language(name)
    sound = gTTS(text=name, lang=tts_lang)
    filename = f'{name}.mp3'
    sound.save(filename)
    playsound(filename)


button_1 = customtkinter.CTkButton(master=frame_1, text='Pronounce it!', command=tts)
button_1.pack(pady=10, padx=10)

app.mainloop()



