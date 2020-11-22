import datetime
import os
import smtplib
import sys
import webbrowser as wb
import pyttsx3
import requests
import speech_recognition as sr
import wikipedia
import webbrowser
import pyautogui
import random
import json
from news import speak_news, getNewsUrl
import time
import pause
import wolframalpha
import playsound
import pyjokes
import time
from time import sleep
from requests import get
import socket
from pyfiglet import  print_figlet
import wolframalpha

api = 'W87V4U-LXQV4YH7UX'
cleint = wolframalpha.Client(api)
engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)


def voice_change(v):
    x = int(v)
    engine.setProperty('voice', voices[x].id)
    speak("here you go boss i have  changed my voice ")


def femalevoice():
    voice_change(2)


def malevoice():
    voice_change(3)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    smg = 'its,', 'today is ', 'it is'
    speak(random.choice(smg))
    speak(date)
    speak(month)
    speak(year)


def checktime(tt):
    hour = datetime.datetime.now().hour
    if ("morning" in tt):
        if (hour >= 6 and hour < 12):
            speak("Good morning Boss")
        else:
            if (hour >= 12 and hour < 18):
                speak("it's Good afternoon boss")
            elif (hour >= 18 and hour < 24):
                speak("it's Good evening boss")
            else:
                speak("it's Goodnight boss")
    elif ("afternoon" in tt):
        if (hour >= 12 and hour < 18):
            speak("it's Good afternoon boss")
        else:
            if (hour >= 6 and hour < 12):
                speak("Good morning boss")
            elif (hour >= 18 and hour < 24):
                speak("Good evening boss")
            else:
                speak("Goodnight boss")
    else:
        speak("night boss!")


# welcome function
def wishme():
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning boss!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon boss")
    elif (hour >= 18 and hour < 24):
        speak("Good evening boss")
    else:
        speak("Goodnight boss")


def WIFI():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        speak('no internet connection')
    else:
        print("Connected, with the IP address: " + IPaddress)


def wishme_end():
    speak("signing off")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon")
    elif (hour >= 18 and hour < 24):
        speak("Good evening")
    else:
        speak("Goodnight.. Sweet dreams")
    quit()


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 9999
        audio = r.listen(source)

    try:
        print("Recognizing...")
        voice_data = r.recognize_google(audio, language='en-in')
        print(f"User said: {voice_data}\n")

    except Exception as e:
        # print(e)
        speak("Say that again please...")
        return "None"
    return voice_data

# weather condition
def weather():
    api_key = "30b2e680ad9c7790ec02fdb4f97f4573"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ('guwahati')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
                                                       " and " + str(weather_description))
        speak(r)
    else:
        speak(" City Not Found ")


def Sweather():
    api_key = "30b2e680ad9c7790ec02fdb4f97f4573"  # generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ('guwahati')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("outside " + " the Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
                                                       " and " + str(weather_description))
        speak(r)
    else:
        speak(" City Not Found ")


def personal():
    speak(
        "I am mark , a voice assistant")


def screenshot():
    img = pyautogui.screenshot()
    img.save(
        "C:\\mark"
    )


def noint():
    IPaddress = socket.gethostbyname(socket.gethostname())
    if IPaddress == "127.0.0.1":
        speak('no internet connection')


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU usage is at ' + usage)
    print('CPU usage is at ' + usage)


def battery():
    battery = psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)
    print("battery is at:" + str(battery.percent))


def jokes():
    j = pyjokes.get_joke()
    print(j)
    speak(j)

def online():
    print_figlet('MARK:)')

from playsound import playsound
import socket as s
import keyboard
online()
def main():
    try:
        os.system('porcupine_demo_mic --keywords blueberry')
        playsound('C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\chime.wav')
        voice_data = takecommand().lower()
        if 'beatbox' in voice_data or 'bit box' in voice_data or 'big box' in voice_data or 'bigbox' in voice_data:
            playsound('C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\preview.mp3')
        if 'repeat' in voice_data:
            voice_data = voice_data.replace("repeat", "")
            voice_data = voice_data.replace("that", "")
            speak(voice_data)

        if ('time') in voice_data:
            strTime = datetime.datetime.now().strftime("%I:%M:%S")
            timemsg = (f', {strTime}'), (f'it is , {strTime}'), (f'the current time is, {strTime}'), (
                f'its , {strTime}')
            speak(random.choice(timemsg))

        elif ('date' in voice_data):
            date()


        elif 'i am sad' in voice_data:
            smg = 'here is something for you ' + jokes(), 'i hate that one', 'i, really dont like it'
            speak(random.choice(smg))


        elif 'i am happy' in voice_data:
            msg = 'Life is full of happiness and tears; be strong and have faith.', 'On a deeper level you are already complete. When you realize that, there is a playful, joyous energy behind what you do', 'Most people are about as happy as they make up their minds to be', 'i am also happy'
            speak(random.choice(msg))


        elif 'i love you' in voice_data:
            reply = 'i also like you', 'i like it', "i don't hate you", 'i also love you as a friend'
            speak(random.choices(reply))


        elif ("tell me about yourself" in voice_data):
            personal()
        elif ("about you" in voice_data):
            personal()


        elif ("who are you" in voice_data):
            personal()


        elif ("yourself" in voice_data):
            personal()


        elif 'tell me the weather in' in voice_data or "tell me today's weather in" in voice_data:
            voice_data = voice_data.replace("weather", "")
            voice_data = voice_data.replace("of", "")
            voice_data = voice_data.replace("at", "")
            voice_data = voice_data.replace("the", "")
            voice_data = voice_data.replace("in", "")
            voice_data = voice_data.replace("city", "")
            voice_data = voice_data.replace("tell", "")
            voice_data = voice_data.replace("me", "")
            voice_data = voice_data.replace("can", "")
            voice_data = voice_data.replace("you", "")
            voice_data = voice_data.replace("today's", "")
            voice_data = voice_data.replace("in", "")

            api_key = "30b2e680ad9c7790ec02fdb4f97f4573"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            city_name = voice_data
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                r = ("in " + city_name + " Temperature is " +
                     str(int(current_temperature - 273.15)) + " degree celsius " +
                     ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
                     ", humidity is " + str(current_humidiy) + " percent"
                                                               " and " + str(weather_description))
                speak(r)

            else:
                speak(" City Not Found ")


        elif 'tell me the weather' in voice_data:
            weather()

        elif 'youtube' in voice_data:
            voice_data = voice_data.replace("youtube", "")
            voice_data = voice_data.replace("search", "")
            voice_data = voice_data.replace("on", "")
            voice_data = voice_data.replace("youtube", "")
            site = 'https://youtube.com/search?q=' + voice_data
            webbrowser.open(site)
        elif 'tell me the temperature' in voice_data:
            weather()


        elif "tell me today's weather" in voice_data:
            weather()


        elif "tell me today's temperature" in voice_data:
            weather()

        if 'wikipedia' in voice_data:
            speak('Searching Wikipedia...')
            voice_data = voice_data.replace("wikipedia", "")
            results = wikipedia.summary(voice_data, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'clock' in voice_data:
            path = 'F:\\digitalClock.py'
            os.startfile(path)



        elif "open website" in voice_data:
            speak("Tell me the name of the website")
            search = takecommand().lower()
            speak('Opening' + search)
            url = 'www.' + search + '.com'
            webbrowser.open(url)


        elif ("song" in voice_data or 'music' in voice_data or 'gana' in voice_data):
            speak("playing a random song")
            path = 'D:\\music\\'
            files = os.listdir(path)
            d = random.choice(files)
            os.startfile('D:\\music\\' + d)


        elif  'clear reminders' in voice_data or 'clear all reminder' in voice_data:
            replyt = 'ok clearing all the reminders ' , 'cleared' , 'cleared all the reminders' 
            speak(random.choice(replyt))
            f = open("data.txt", "r+")  
            f.seek(0)    
            f.truncate()  

        elif ("create a reminder list" in voice_data or "set a reminder" in voice_data):
            speak("What is the reminder?")
            data = takecommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()



        elif 'full form of friday' in voice_data:
            speak('Female Replacement Intelligent Digital Assistant Youth')


        elif 'face' in voice_data:
            speak('opening face recognition')
            path = 'F:\\detect_face_video.py'
            os.startfile(path)


        elif ("do you know anything" in voice_data or "remember" in voice_data):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())




        elif ("powers" in voice_data or "help" in voice_data
              or "features" in voice_data or 'what can you do' in voice_data):
            features = ''' i can help to do lot many things like..
                i can tell you the current time and date,
                i can tell you the current weather,
                i can tell you battery and cpu usage,
                i can create the reminder list,
                i can shut down or logout or hibernate your system,
                i can tell you non funny jokes,
                i can open any website,
                i can repeat what you  you told me,
                i can search the thing on wikipedia,
                i can change my voice from male to female and vice-versa
                i have  a search engine make by my boss if you want to know something just say open search and ask the question
                i have a wake word detection i will be online if you say hey mark
                And yes one more thing, My boss is working on this system to add more features...,
                tell me what can i do for you??
                '''
            speak(features)



        elif ("voice" in voice_data):
            if 'female' in voice_data:
                femalevoice()

            else:
                malevoice()


        elif ('i am done' in voice_data or 'bye bye mark' in voice_data
              or 'go offline mark' in voice_data or 'bye' in voice_data):
                sys.exit()

        elif ("how's your day going" in voice_data or 'how is your day going' in voice_data):
            speak('Wonderfull , thanks for asking me, how can i help you ')


        elif 'change name' in voice_data:
            f = open("C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\name.txt", "r+")
            f.seek(0)
            f.truncate()
            speak('tell me your name')
            sname = takecommand()()
            try:
                if 'neelam' in sname:
                    file1 = open("C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\name.txt", "w")
                    file1.write(sname)
                    file1.close()
                    file_contents = f.read()
                    speak('from now i will call you sir' + file_contents)

            except Exception as e:
                file1 = open("C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\name.txt", "w")
                file1.write(sname)
                file1.close()
                file_contents = f.read()
                speak('from now i will call you sir' + file_contents)



        elif 'change birthday' in voice_data:
            f = open("C:\\MARK\\birthday.txt", "r+")
            f.seek(0)
            f.truncate()
            speak('tell me the birthday date')
            sname = takecommand()()
            file1 = open("C:\\MARK\\birthday.txt", "w")
            file1.write(sname)
            file1.close()
            file_contents = f.read()
            speak('so your birthday is at' + file_contents)

        elif 'my birthday' in voice_data:
            f = open('C:\\MARK\\birthday.txt', 'r')
            file_contents = f.read()
            speak(file_contents)


        elif 'hey there' in voice_data:
            speak('hello there')


        elif 'tell me my name' in voice_data:
            f = open('C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\name.txt', 'r')
            file_contents = f.read()
            speak(file_contents)


        elif 'what is my name' in voice_data:
            f = open('C:\\MARK\\my name.txt', 'r')
            file_contents = f.read()
            speak(file_contents)


        elif 'shutdown' in voice_data or 'turn off' in voice_data or '':
            speak('system offline')
            os.system("shutdown /p")


        elif 'open instagram' in voice_data:
            speak('opening Instagram')
            webbrowser.open('https://www.instagram.com/?hl=en')


        elif 'full form of jarvis' in voice_data:
            speak('Just A Rather Very Intelligent System')


        elif 'news' in voice_data:
            speak('here you go sir')
            path = 'C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\news.py'
            os.startfile(path)



        elif 'screenshot' in voice_data:
            speak('ok sir')
            screenshot()


        elif 'cpu' in voice_data:
            cpu()


        elif ('there' in voice_data or 'dear' in voice_data):
            speak('For you Sir always')


        elif 'battery' in voice_data:
            battery()


        elif 'joke' in voice_data:
            jokes()



        elif 'open location' in voice_data:
            speak('tell me the location you are looking for')
            location = takecommand()()
            url2 = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open(url2)
            speak('location on your screen boss')

        elif 'close browser' in voice_data:
            try:
                speak('as you wish')
                os.system('TASKKILL /F /IM msedge.exe')

            except Exception as e:
                speak("i cant do that right now")

        elif 'close all' in voice_data:
            try:
                speak('as you wish')
                os.system('TASKKILL /F /IM *')

            except Exception as e:
                speak("i cant do that right now")
        elif 'close file' in voice_data:
            try:
                speak('as you wish')
                os.system('TASKKILL /F /IM Explorer.exe')

            except Exception as e:
                speak("i cant do that right now")

        elif 'my location' in voice_data:
            speak('opening your home location on browser')
            loc = 'https://www.google.co.in/maps/@26.1317482,91.8018681,18.5z'
            webbrowser.open(loc)


        elif 'google' in voice_data:
            voice_data = voice_data.replace("google", "")
            voice_data = voice_data.replace("it", "")
            speak('here you go ')
            url69 = 'https://google.com/search?q=' + voice_data
            webbrowser.open(url69)



        elif 'switch window' in voice_data:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            pyautogui.press("right")
            pyautogui.keyUp("alt")
            speak('window switched')


        elif 'close' in voice_data:
            pyautogui.keyDown("alt")
            pyautogui.press("F4")
            pyautogui.keyUp()
            speak('application killed')


        elif 'what is your name' in voice_data:
            speak('MY NAME is Mark')


        elif 'whatsapp' in voice_data:
            speak('opening whatsapp')
            wpath = 'C:\\Users\\admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe'
            os.startfile(wpath)

        elif 'wish birthday' in voice_data:
            speak('this is for you')
            path = 'D:\\project Friday\\Y2Mate (mp3cut.net) (1).mp3'
            os.startfile(path)


        elif 'tell me my birthday' in voice_data:
            speak('i remember that you told me your birthday is at 20th march')


        elif 'folder' in voice_data:
            speak('tell me the name of the folder')
            path = 'C:\\Users\\ADMIN\\Desktop'
            os.chdir(path)
            Newfolder = takecommand()()
            os.makedirs(Newfolder)
            speak('i have  made a folder named' + Newfolder + 'in you dekstop directry')


        elif 'hello mark' in voice_data or 'lo mark' in voice_data:
            speak("hello sir how's going")


        elif 'hey  mark' in voice_data:
            speak('hey sir what can i do for you')


        elif 'editor' in voice_data or 'visual studio code' in voice_data:
            speak('opening code editor')
            os.startfile('C:\\Users\\ADMIN\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe')


        elif 'cmd' in voice_data or 'command' in voice_data:
            os.startfile('cmd.exe')


        elif 'red or blue' in voice_data:
            speak('BLue sir')


        elif 'your favorite colour' in voice_data or 'tell me your favourite colour' in voice_data:
            speak('blue')


        elif 'change colour' in voice_data:
            os.system('color 03')

        elif 'how are you' in voice_data:
            msg = "i'm well how are you?", "i'm good", " nice , how's your day going", 'Wonderfull', 'excellent', 'great,thanks for asking'
            speak(random.choice(msg))


        elif 'ip address' in voice_data:
            ip = get('https://api.ipify.org').text
            speak(f'your ip address is {ip}"')


        elif 'hello' in voice_data:
            speak('hello boss')

        if 'restart' in voice_data:
            os.startfile("C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py")

        if 'amazon order' in voice_data:
            url = 'https://www.amazon.in/gp/css/order-history?ref_=nav_orders_first'
            webbrowser.open(url)
            sys.exit

        if 'wake up' in voice_data:
            speak('Online and ready boss')

        if "you can't do anything" in voice_data or 'you are nothing' in voice_data or 'you are dumb' in voice_data or 'you dont have brain' in voice_data or 'you are mad' in voice_data:
            speak("Sorry boss")


        elif 'wake word' in voice_data:
            speak('my wake word is : hey mark')



        elif 'sleep' in voice_data:
            speak('As you wish, for now i will sleep if you want me you can call me ')


        elif 'boreing' in voice_data:
            speak('lets play some music')
        elif 'email' in voice_data:
            speak('are you the sender?')
            sender = takecommand()()

            if 'yes' in sender:
                try:
                    speak("Please Enter Email address of Recipient.")
                    Recipient_user = takecommand()
                    speak('What should I say? ')
                    content = takecommand()()

                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("gmail", 'pass')
                    server.sendmail('nilavdas5@gmail.com', Recipient_user, content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry boss i cant send this email right now!')
            pause.seconds(1)

        elif 'hide file' in voice_data or 'hide all file' in voice_data or 'hide files' in voice_data or 'visible file' in voice_data or 'unhide all  files' in voice_data:
            if 'hide' in voice_data:
                os.system("attrib +h /s /d")
                cms = 'all files are hidden' , 'i hidden all the files' , 'all files are hidden now'
                speak(random.choice(cms))
            if 'visibile' in voice_data:
                os.system('attrib +h /s /d')
            

        elif ('what' in voice_data or 'who' in voice_data or 'when' in voice_data or 'how' in voice_data or 'where' in voice_data or 'tell' in voice_data):
            if'what is the time' in voice_data: 
                main()
            if'how are you' in voice_data: 
                main()
            if'tell me the time' in voice_data: 
                main()
            if'what is weather' in voice_data: 
                main()
            if'tell me the weather' in voice_data: 
                main()
            try:
                try:
                    speak('Getting information')
                    res = cleint.query(voice_data)
                    results = next(res.results).text
                    speak(results)
                except:
                    results = wikipedia.summary(voice_data, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
            except Exception :
                speak("sorry i don't know that")
    except Exception:
        msgg = 'sorry i cant do that right now' , 'error404'
        speak(random.choice(msgg))

if __name__ == "__main__":
    while True:
        noint()
        main()
        
