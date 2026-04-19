# Voice-Controlled-Mobile-Robot
A voice-controlled robot interface built with Python. Uses speech recognition for hands-free command input and text-to-speech for audio feedback. Features password-protected access, directional and geometric movement commands, coordinate/angle input, real-time weather via OpenWeatherMap, battery monitoring, and a built-in storyteller.

# 🤖 Voice-Controlled Robot Interface

A Python-based voice command system that lets you control a robot entirely through speech. Features secure voice-authenticated access, movement commands, geometric path drawing, weather queries, battery monitoring, and a built-in story mode — all driven by real-time speech recognition and text-to-speech feedback.

---

## Features

- **Voice Authentication** — Password-protected access with up to 3 spoken attempts before lockout
- **Movement Commands** — Forward, backward, left, right
- **Geometric Paths** — Circle, rectangle, triangle, square, dance
- **Coordinate & Angle Control** — Spoken translate (x, y) and rotate (angle°) commands
- **Battery Monitor** — Reports battery level and warns when below 20%
- **Weather Integration** — Live weather via OpenWeatherMap API (city spoken by voice)
- **Story Mode** — Reads a built-in story on request
- **Full TTS Feedback** — Every action is confirmed aloud via `pyttsx3`

---

## Requirements

### Python Version
Python 3.7+

### Dependencies

Install all dependencies with:

```bash
pip install speechrecognition pyttsx3 requests pyaudio
```

| Package            | Purpose                          |
|--------------------|----------------------------------|
| `speechrecognition`| Captures and transcribes speech  |
| `pyttsx3`          | Text-to-speech engine            |
| `requests`         | Weather API HTTP calls           |
| `pyaudio`          | Microphone input backend         |

> **Note for Linux users:** You may need to install `portaudio` first:
> ```bash
> sudo apt-get install portaudio19-dev python3-pyaudio
> ```

> **Note for Windows users:** If `pyaudio` fails to install via pip, download the appropriate `.whl` from [Gohlke's repository](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install manually.

---

## Setup

1. **Clone or download** this repository.

2. **Install dependencies** (see above).

3. **Get an OpenWeatherMap API key:**
   - Sign up for free at [openweathermap.org](https://openweathermap.org/api)
   - Replace the placeholder in the script:
     ```python
     api_key = "YOUR_API_KEY_HERE"
     ```

4. **Change the password** (optional but recommended):
   ```python
   correct_password = "python"  # Change this to your preferred password
   ```

5. **Run the script:**
   ```bash
   python robot_voice_control.py
   ```

---

## Usage

### Startup Flow

```
Program speaks  →  You say your name
Program speaks  →  You say the password (up to 3 attempts)
Program speaks  →  Robot initializes and prompts for commands
```

### Available Voice Commands

| Command       | Action                                        |
|---------------|-----------------------------------------------|
| `forward`     | Move robot forward                            |
| `backward`    | Move robot backward                           |
| `left`        | Turn robot left                               |
| `right`       | Turn robot right                              |
| `dance`       | Spin in circles                               |
| `circle`      | Move in a circular path                       |
| `rectangle`   | Move in a rectangular path                    |
| `triangle`    | Move in a triangular path                     |
| `square`      | Move in a square path                         |
| `translate`   | Move to spoken (x, y) coordinates             |
| `rotate`      | Rotate by a spoken angle in degrees           |
| `battery`     | Report current battery level                  |
| `weather`     | Get live weather for a spoken city name       |
| `story`       | Listen to the Tortoise and the Hare           |
| `stop`        | Shut down the command loop                    |

---

## Project Structure

```
robot_voice_control.py   # Main script — all logic in one file
README.md                # This file
```

---

## Known Limitations

- Speech recognition requires an active internet connection (uses Google Speech API).
- `pyttsx3` voice quality depends on the TTS voices installed on your OS.
- Battery level is randomly simulated — wire in real sensor data via the `battery_level` variable for physical robots.
- The weather command requires a valid OpenWeatherMap API key.
- Background noise may affect recognition accuracy; use the script in a quiet environment.

---

## Future Improvements

- Replace Google Speech API with an offline recognizer (e.g., Vosk) for standalone use
- Integrate real encoder/motor feedback for actual movement execution
- Add a GUI dashboard for command history and battery visualization
- Support multiple languages via configurable TTS voices
- ROS2 / serial bridge for physical robot hardware

---

## License

This project is open for personal and educational use. Attribution appreciated.
