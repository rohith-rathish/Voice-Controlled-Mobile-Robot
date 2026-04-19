import speech_recognition as sr
import pyttsx3
import requests
import random  # Fix 1: was missing

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def speak(text):
    print(f"Program: {text}")
    tts_engine.say(text)
    tts_engine.runAndWait()

# ──────────────────────────────────────────────
# Movement functions  (Fix 2: moved out of the
# if-block so they're always accessible)
# ──────────────────────────────────────────────

def move_forward():
    speak("Moving forward.")
    print("\nRobot moves forward.\n")

def move_backward():
    speak("Moving backward.")
    print("\nRobot moves backward.\n")

def move_left():
    speak("Turning left.")
    print("\nRobot turns left.\n")

def move_right():
    speak("Turning right.")
    print("\nRobot turns right.\n")

def dance():
    speak("Dancing in circles!")
    print("\nRobot spins in circles as a dance.\n")

def draw_circle():
    speak("The robot will move in a circle.")
    print("\nRobot moves in a circular pattern.\n")

def draw_rectangle():
    speak("The robot will move in a rectangle.")
    print("\nRobot moves in a rectangular pattern.\n")

def draw_triangle():
    speak("The robot will move in a triangle.")
    print("\nRobot moves in a triangular pattern.\n")

def draw_square():
    speak("The robot will move in a square.")
    print("\nRobot moves in a square pattern.\n")

def translate(x, y):
    speak(f"Translating to coordinates ({x}, {y}).")
    print(f"\nRobot moves to coordinates ({x}, {y}).\n")

def rotate(angle):
    speak(f"Rotating by {angle} degrees.")
    print(f"\nRobot rotates by {angle} degrees.\n")

def get_coordinates():
    while True:
        speak("Please say the x coordinate.")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                x = int(recognizer.recognize_google(audio))
                print(f"You said x coordinate: {x}")
                break
            except (ValueError, sr.UnknownValueError):
                speak("Sorry, I didn't catch that. Please repeat the x coordinate.")

    while True:
        speak("Please say the y coordinate.")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            try:
                y = int(recognizer.recognize_google(audio))
                print(f"You said y coordinate: {y}")
                break
            except (ValueError, sr.UnknownValueError):
                speak("Sorry, I didn't catch that. Please repeat the y coordinate.")

    return x, y

def get_angle():
    speak("Please say the angle.")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            angle = int(recognizer.recognize_google(audio))
            print(f"You said angle: {angle}")
            return angle
        except (ValueError, sr.UnknownValueError):
            speak("Sorry, I didn't catch that. Please repeat the angle.")
            return get_angle()

# ──────────────────────────────────────────────
# Battery, weather, story
# ──────────────────────────────────────────────

battery_level = random.randint(1, 100)  # Fix 3: random now imported

def check_battery():
    global battery_level
    speak(f"The current battery level is {battery_level} percent.")
    if battery_level < 20:
        speak("Warning! Battery level is low. Please recharge soon.")

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        speak(f"The current weather in {city} is {weather} with a temperature of {temperature} degrees Celsius.")
    else:
        speak("Sorry, I couldn't retrieve the weather information at this time.")

def tell_story():
    story = ("Once upon a time, there was a speedy hare who bragged about how fast he could run. "
             "Tired of hearing him boast, the tortoise challenged him to a race. "
             "The hare laughed at the slow tortoise and agreed to the race. "
             "As they started, the hare dashed ahead and decided to take a nap, confident he would win. "
             "Meanwhile, the tortoise kept going slowly but steadily. "
             "When the hare woke up, he saw that the tortoise was near the finish line. "
             "He ran as fast as he could, but it was too late. The tortoise won the race! "
             "The moral of the story is that slow and steady wins the race.")
    speak(story)

# ──────────────────────────────────────────────
# Command listener
# ──────────────────────────────────────────────

def listen_for_movement():
    speak("Please give a movement command.")
    with sr.Microphone() as source:
        print("Listening for movement command...\n")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}\n")

            if "forward" in command:
                move_forward()
            elif "backward" in command:
                move_backward()
            elif "left" in command:
                move_left()
            elif "right" in command:
                move_right()
            elif "dance" in command:
                dance()
            elif "circle" in command:
                draw_circle()
            elif "rectangle" in command:
                draw_rectangle()
            elif "triangle" in command:
                draw_triangle()
            elif "square" in command:
                draw_square()
            elif "translate" in command:
                x, y = get_coordinates()
                translate(x, y)
            elif "rotate" in command:
                angle = get_angle()
                rotate(angle)
            elif "battery" in command:
                check_battery()
            elif "weather" in command:
                speak("Please say the city name.")
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    try:
                        city = recognizer.recognize_google(audio)
                        print(f"You said city: {city}\n")
                        api_key = "28a602077c50611f6b54d38a9019aa37"
                        get_weather(api_key, city)
                    except sr.UnknownValueError:
                        speak("Sorry, I didn't catch that. Please repeat the city name.")
            elif "story" in command:
                tell_story()
            elif "stop" in command:
                speak("Stopping the robot.")
                return False
            else:
                speak("Sorry, I didn't understand the command.")
                print("Unrecognized movement command.\n")

        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Could you repeat?")
        except sr.RequestError:
            speak("There seems to be a connection issue.")

    return True

# ──────────────────────────────────────────────
# Startup: name
# ──────────────────────────────────────────────

speak("Hello! What is your name?")

name = None
with sr.Microphone() as source:
    print("Listening for your name...\n")
    audio = recognizer.listen(source)
    try:
        name = recognizer.recognize_google(audio)
        print(f"You said: {name}\n")
        speak(f"Nice to meet you, {name}. Please say the password to gain access.")
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
    except sr.RequestError:
        speak("Sorry, there seems to be a connection issue.")

# ──────────────────────────────────────────────
# Password gate
# ──────────────────────────────────────────────

# Fix 4: initialise attempts at top level so it's always defined
attempts = 0
max_attempts = 3
correct_password = "python"

if name:
    while attempts < max_attempts:
        with sr.Microphone() as source:
            print("Listening for the password...\n")
            audio = recognizer.listen(source)
            try:
                password = recognizer.recognize_google(audio)
                print(f"You said: {password}\n")
                if password.lower() == correct_password:  # Fix 5: case-insensitive compare
                    speak("Access granted. Welcome to the voice-controlled robot.")
                    break
                else:
                    attempts += 1
                    speak(f"Incorrect password. You have {max_attempts - attempts} attempts left.")
            except sr.UnknownValueError:
                speak("I couldn't understand you. Please try again.")
                attempts += 1
            except sr.RequestError:
                speak("Sorry, there seems to be a connection issue.")
                break

    if attempts >= max_attempts:  # Fix 6: >= instead of == (safer)
        speak("Access denied. You have reached the maximum number of attempts.")
        exit()

# ──────────────────────────────────────────────
# Main loop
# ──────────────────────────────────────────────

speak("The robot is initializing...")
speak("Loading...")
speak(
    "Please give a movement command: forward, backward, left, right, or a special movement "
    "like dance, circle, rectangle, triangle, square. You can also say translate or rotate, "
    "or say stop to end. You can also ask for battery status, weather, or a story."
)

while listen_for_movement():
    pass
