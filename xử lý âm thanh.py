import speech_recognition as sr
class AmThanhToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def chuyen_doi(self):
        with sr.Microphone() as source:
            print("Bắt đầu nhận diện âm thanh")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            text = self.recognizer.recognize_google(audio, language="vi-VN")
            print("Văn bản nhận được:", text)
        except sr.UnknownValueError:
            print("Không thể nhận dạng âm thanh.")
