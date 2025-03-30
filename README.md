# MurfTone

## Overview
MurfTone is a text-to-speech (TTS) application using the **Murf API**. It allows users to convert text into high-quality speech with various voice moods and styles.

## Features
- Supports multiple voice profiles (e.g., Hazel, Cooper)
- Allows mood selection for each voice
- Uses **Flet** for UI and **Flet Audio** for playback
- Retrieves available voices from the Murf API

## Installation

### 1. Clone the Repository
```sh
git clone <your-repository-url>
cd MurfTone
```

### 2. Install Dependencies
Run the following command to install all required packages:
```sh
pip install -r requirements.txt
```

If `requirements.txt` is missing, you can manually install:
```sh
pip install flet requests murf flet_audio
```

### 3. Set Up API Key
Create a `.env` file or modify `api_key.py`:
```python
API_KEY = "Paste your API Key here"
```

## Usage
Run the main script:
```sh
python main.py
```

## Dependencies
- `flet` (UI framework)
- `requests` (API communication)
- `murf` (Text-to-speech processing)
- `flet_audio` (Audio playback)

## Notes
- Make sure to have a valid **Murf API key**.
- If you encounter errors, check dependencies using:
  ```sh
  pip list
  ```

## License  
This project is licensed under the **MIT License** – see the [LICENSE](sandbox:/mnt/data/LICENSE) file for details.  
