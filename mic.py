import speech_recognition as sr
import cv2
detect=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(len(detect))
DATADIR = "data"
from string import ascii_lowercase
LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return ' '.join(numbers)
# All the categories you want your neural network to detect
CATEGORIES = ["0","1","2","3","4","5","6","7","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
r = sr.Recognizer()
speech = sr.Microphone(device_index=1)
with speech as source:
    print("say something!…")
    audio = r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
try:
    recog = r.recognize_google(audio, language = 'en-US')

    print("You said: " + recog)
    for x in recog:
        if x not in " ":
            l=alphabet_position(x)
            k=int(l)-1
            print(k)
            img='audio/'+str(k)+'.jpg'
            image = cv2.imread(img)
            window_name = 'image'
            cv2.imshow(window_name, image)
            cv2.waitKey(1500)
            #closing all open windows
            cv2.destroyAllWindows()
            
        
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))