import pyttsx3

engine = pyttsx3.init()

print("Напиши текст — он будет озвучен")
print("Напиши 'exit' чтобы выйти\n")

while True:
    text = input("Что сказать? ➤ ")

    if text.lower() == "exit":
        print("Выход...")
        break

    engine.say(text)
    engine.runAndWait()
