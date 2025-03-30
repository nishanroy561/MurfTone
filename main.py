import flet as ft
import requests
import os
from murf import Murf
from api_key import API_KEY
import flet_audio as fta

client = Murf(api_key=API_KEY)
voices = client.text_to_speech.get_voices()

# for voice in voices:
#     print(f"Voice ID: {voice.voice_id}, Name: {voice.display_name}, Moods: {voice.available_styles}")

VOICE_MOODS = {
    "Hazel": {
        "voice_id": "en-UK-hazel",
        "moods": ['Conversational']
    },
    "Cooper": {
        "voice_id": "en-US-cooper",
        "moods": ['Conversational', 'Promo', 'Angry', 'Inspirational', 'Sad', 'Newscast']
    },
    "Imani": {
        "voice_id": "en-US-imani",
        "moods": ['Conversational']
    },
    "Giorgio": {
        "voice_id": "it-IT-giorgio",
        "moods": ['Conversational']
    },
    "Arnab": {
        "voice_id": "bn-IN-arnab",
        "moods": ['Conversational']
    },
    "Wayne": {
        "voice_id": "en-US-wayne",
        "moods": ['Conversational', 'Narration', 'Inspirational', 'Promo', 'NewsCast', 'Calm', 'Sad', 'Angry']
    },
    "Shivani": {
        "voice_id": "en-IN-shivani",
        "moods": ['Conversational']
    },
    "Daniel": {
        "voice_id": "en-US-daniel",
        "moods": ['Conversational', 'Inspirational', 'Sad', 'Storytelling']
    },
    "Marija": {
        "voice_id": "hr-HR-marija",
        "moods": ['Narration']
    },
    "Anwesha": {
        "voice_id": "bn-IN-anwesha",
        "moods": ['Conversational']
    },
    "Alejandro": {
        "voice_id": "es-MX-alejandro",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Joyce": {
        "voice_id": "en-AU-joyce",
        "moods": ['Conversational', 'Narration']
    },
    "Zion": {
        "voice_id": "en-US-zion",
        "moods": ['Promo', 'Narration']
    },
    "Isha": {
        "voice_id": "en-IN-isha",
        "moods": ['Conversational']
    },
    "Riley": {
        "voice_id": "en-US-riley",
        "moods": ['Promo', 'Narration']
    },
    "Hwan": {
        "voice_id": "ko-KR-hwan",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Adelie": {
        "voice_id": "fr-FR-adélie",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Carter": {
        "voice_id": "en-US-carter",
        "moods": ['Conversational', 'Narration', 'Documentary', 'Calm']
    },
    "Gabriel": {
        "voice_id": "en-UK-gabriel",
        "moods": ['Documentary', 'Promo', 'Evil']
    },
    "Juliet": {
        "voice_id": "en-UK-juliet",
        "moods": ['Conversational']
    },
    "Arohi": {
        "voice_id": "en-IN-arohi",
        "moods": ['Conversational', 'Promo']
    },
    "Maxime": {
        "voice_id": "fr-FR-maxime",
        "moods": ['Conversational']
    },
    "Josephine": {
        "voice_id": "de-DE-josephine",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Hugo": {
        "voice_id": "en-UK-hugo",
        "moods": ['Conversational']
    },
    "Samantha": {
        "voice_id": "en-US-samantha",
        "moods": ['Conversational', 'Luxury', 'Promo', 'Angry', 'Sad', 'Newscast']
    },
    "Erna": {
        "voice_id": "de-DE-erna",
        "moods": ['Conversational']
    },
    "Baolin": {
        "voice_id": "zh-CN-baolin",
        "moods": ['Conversational', 'Promo', 'Sad']
    },
    "Isadora": {
        "voice_id": "pt-BR-isadora",
        "moods": ['Conversational']
    },
    "Vincenzo": {
        "voice_id": "it-IT-vincenzo",
        "moods": ['Conversational']
    },
    "Terrell": {
        "voice_id": "en-US-terrell",
        "moods": ['Inspirational', 'Narration', 'Calm', 'Promo', 'Conversational']
    },
    "Denzel": {
        "voice_id": "en-US-denzel",
        "moods": ['Promo', 'Conversational']
    },
    "Heidi": {
        "voice_id": "en-UK-heidi",
        "moods": ['Conversational']
    },
    "Miles": {
        "voice_id": "en-US-miles",
        "moods": ['Conversational', 'Promo', 'Sports Commentary', 'Narration', 'Newscast', 'Sad', 'Angry', 'Calm', 'Terrified', 'Inspirational', 'Pirate']
    },
    "Abigail": {
        "voice_id": "en-US-abigail",
        "moods": ['Narration', 'Conversational']
    },
    "Justine": {
        "voice_id": "fr-FR-justine",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad', 'Angry']
    },
    "Greta": {
        "voice_id": "it-IT-greta",
        "moods": ['Conversational']
    },
    "Shane": {
        "voice_id": "en-AU-shane",
        "moods": ['Conversational', 'Narration']
    },
    "Peter": {
        "voice_id": "en-UK-peter",
        "moods": ['Conversational']
    },
    "Famke": {
        "voice_id": "nl-NL-famke",
        "moods": ['Conversational']
    },
    "Ivy": {
        "voice_id": "en-AU-ivy",
        "moods": ['Conversational', 'Promo', 'Calm', 'Angry', 'Sad']
    },
    "Dirk": {
        "voice_id": "nl-NL-dirk",
        "moods": ['Conversational']
    },
    "Axel": {
        "voice_id": "fr-FR-axel",
        "moods": ['Conversational']
    },
    "Carla": {
        "voice_id": "es-ES-carla",
        "moods": ['Conversational']
    },
    "Claire": {
        "voice_id": "en-US-claire",
        "moods": ['Narration', 'Luxury']
    },
    "Jangmi": {
        "voice_id": "ko-KR-jangmi",
        "moods": ['Conversational']
    },
    "Sanghoon": {
        "voice_id": "ko-KR-sanghoon",
        "moods": ['Conversational', 'Promo']
    },
    "Denki": {
        "voice_id": "ja-JP-denki",
        "moods": ['Conversational']
    },
    "Vera": {
        "voice_id": "it-IT-vera",
        "moods": ['Conversational']
    },
    "Rahul": {
        "voice_id": "hi-IN-rahul",
        "moods": ['Conversational']
    },
    "Elvira": {
        "voice_id": "es-ES-elvira",
        "moods": ['Conversational', 'Promo']
    },
    "Enrique": {
        "voice_id": "es-ES-enrique",
        "moods": ['Conversational', 'Promo', 'Calm']
    },
    "Aiden": {
        "voice_id": "en-UK-aiden",
        "moods": ['Narration', 'Character']
    },
    "Ronnie": {
        "voice_id": "en-US-ronnie",
        "moods": ['Promo', 'Conversational', 'Angry', 'Sad', 'NewsCast']
    },
    "Amber": {
        "voice_id": "en-UK-amber",
        "moods": ['Documentary']
    },
    "Shweta": {
        "voice_id": "hi-IN-shweta",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Amit": {
        "voice_id": "hi-IN-amit",
        "moods": ['Conversational']
    },
    "Jimm": {
        "voice_id": "en-AU-jimm",
        "moods": ['Conversational', 'Narration']
    },
    "Pearl": {
        "voice_id": "en-UK-pearl",
        "moods": ['Storytelling']
    },
    "Benicio": {
        "voice_id": "pt-BR-benício",
        "moods": ['Conversational']
    },
    "Freddie": {
        "voice_id": "en-UK-freddie",
        "moods": ['Conversational']
    },
    "Ryan": {
        "voice_id": "en-US-ryan",
        "moods": ['Narration', 'Conversational', 'Promo', 'Angry', 'Sad']
    },
    "Eloa": {
        "voice_id": "pt-BR-eloa",
        "moods": ['Conversational', 'Promo']
    },
    "Charlotte": {
        "voice_id": "en-US-charlotte",
        "moods": ['Narration']
    },
    "Lia": {
        "voice_id": "de-DE-lia",
        "moods": ['Conversational']
    },
    "Natalie": {
        "voice_id": "en-US-natalie",
        "moods": ['Promo', 'Narration', 'Newscast Formal', 'Meditative', 'Sad', 'Angry', 'Conversational', 'Newscast Casual', 'Furious', 'Sorrowful', 'Terrified', 'Inspirational']
    },
    "Michelle": {
        "voice_id": "en-US-michelle",
        "moods": ['Conversational']
    },
    "Phoebe": {
        "voice_id": "en-US-phoebe",
        "moods": ['Conversational']
    },
    "Carmen": {
        "voice_id": "es-ES-carmen",
        "moods": ['Conversational']
    },
    "Caleb": {
        "voice_id": "en-US-caleb",
        "moods": ['Promo', 'Conversational']
    },
    "Iris": {
        "voice_id": "en-US-iris",
        "moods": ['Friendly', 'Conversational', 'Narration']
    },
    "Harrison": {
        "voice_id": "en-UK-harrison",
        "moods": ['Conversational']
    },
    "Marcus": {
        "voice_id": "en-US-marcus",
        "moods": ['Conversational', 'Narration']
    },
    "Josie": {
        "voice_id": "en-US-josie",
        "moods": ['Narration', 'Conversational']
    },
    "Ariana": {
        "voice_id": "en-US-ariana",
        "moods": ['Conversational', 'Narration']
    },
    "Daisy": {
        "voice_id": "en-US-daisy",
        "moods": ['Conversational', 'Promo', 'Narration', 'NewsCast', 'Sad']
    },
    "Charles": {
        "voice_id": "en-US-charles",
        "moods": ['Conversational', 'Promo', 'Calm', 'NewsCast', 'Inspirational', 'Sad', 'Angry']
    },
    "Reggie": {
        "voice_id": "en-UK-reggie",
        "moods": ['Promo']
    },
    "Tibor": {
        "voice_id": "sk-SK-tibor",
        "moods": ['Narration']
    },
    "Julia": {
        "voice_id": "en-US-julia",
        "moods": ['Narration', 'Witch', 'Conversational', 'Promo', 'Storytelling', 'Calm', 'Newscast', 'Angry', 'Sad']
    },
    "Emily": {
        "voice_id": "en-SCOTT-emily",
        "moods": ['Conversational']
    },
    "Dylan": {
        "voice_id": "en-US-dylan",
        "moods": ['Documentary', 'Conversational', 'Inspirational', 'Newscast']
    },
    "Valeria": {
        "voice_id": "es-MX-valeria",
        "moods": ['Conversational']
    },
    "Eashwar": {
        "voice_id": "en-IN-eashwar",
        "moods": ['Conversational']
    },
    "Evelyn": {
        "voice_id": "en-AU-evelyn",
        "moods": ['Conversational']
    },
    "Lara": {
        "voice_id": "de-DE-lara",
        "moods": ['Conversational']
    },
    "Evander": {
        "voice_id": "en-US-evander",
        "moods": ['Friendly', 'Narration', 'Conversational']
    },
    "Rory": {
        "voice_id": "en-SCOTT-rory",
        "moods": ['Conversational']
    },
    "Yago": {
        "voice_id": "pt-BR-yago",
        "moods": ['Conversational']
    },
    "Iniya": {
        "voice_id": "ta-IN-iniya",
        "moods": ['Conversational']
    },
    "Leyton": {
        "voice_id": "en-AU-leyton",
        "moods": ['Conversational', 'Narration', 'Calm', 'Angry', 'Sad', 'Promo', 'Newscast', 'Terrified', 'Inspirational']
    },
    "Louise": {
        "voice_id": "fr-FR-louise",
        "moods": ['Conversational']
    },
    "Wei": {
        "voice_id": "zh-CN-wei",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Gyeong": {
        "voice_id": "ko-KR-gyeong",
        "moods": ['Conversational']
    },
    "Matthias": {
        "voice_id": "de-DE-matthias",
        "moods": ['Conversational', 'Promo', 'Calm', 'Angry']
    },
    "Rohan": {
        "voice_id": "en-IN-rohan",
        "moods": ['Conversational']
    },
    "Delilah": {
        "voice_id": "en-US-delilah",
        "moods": ['Narration', 'Conversational']
    },
    "Paul": {
        "voice_id": "en-US-paul",
        "moods": ['Narration']
    },
    "Abhik": {
        "voice_id": "bn-IN-abhik",
        "moods": ['Conversational']
    },
    "Angela": {
        "voice_id": "en-US-angela",
        "moods": ['Promo']
    },
    "Naomi": {
        "voice_id": "en-US-naomi",
        "moods": ['Conversational', 'Inspirational']
    },
    "Carlos": {
        "voice_id": "es-MX-carlos",
        "moods": ['Conversational']
    },
    "Merel": {
        "voice_id": "nl-NL-merel",
        "moods": ['Conversational']
    },
    "Kenji": {
        "voice_id": "ja-JP-kenji",
        "moods": ['Conversational']
    },
    "Alicia": {
        "voice_id": "en-US-alicia",
        "moods": ['Conversational', 'Angry', 'Calm']
    },
    "Alia": {
        "voice_id": "en-IN-alia",
        "moods": ['Promo', 'Documentary']
    },
    "Jiao": {
        "voice_id": "zh-CN-jiao",
        "moods": ['Conversational']
    },
    "June": {
        "voice_id": "en-US-june",
        "moods": ['Promo']
    },
    "Ashton": {
        "voice_id": "en-AU-ashton",
        "moods": ['Narration', 'Promo']
    },
    "Finley": {
        "voice_id": "en-UK-finley",
        "moods": ['Promo', 'Conversational', 'Angry', 'Sad']
    },
    "Blazej": {
        "voice_id": "pl-PL-blazej",
        "moods": ['Conversational']
    },
    "Stavros": {
        "voice_id": "el-GR-stavros",
        "moods": ['Narration']
    },
    "Zhang": {
        "voice_id": "zh-CN-zhang",
        "moods": ['Conversational', 'Promo', 'Calm']
    },
    "Sophia": {
        "voice_id": "en-AU-sophia",
        "moods": ['Narration']
    },
    "Kylie": {
        "voice_id": "en-AU-kylie",
        "moods": ['Conversational']
    },
    "Jayden": {
        "voice_id": "en-US-jayden",
        "moods": ['Narration', 'Friendly', 'Conversational']
    },
    "Aarav": {
        "voice_id": "en-IN-aarav",
        "moods": ['Conversational']
    },
    "Bjorn": {
        "voice_id": "de-DE-björn",
        "moods": ['Conversational', 'Promo']
    },
    "Ishani": {
        "voice_id": "bn-IN-ishani",
        "moods": ['Conversational']
    },
    "Yuxan": {
        "voice_id": "zh-CN-yuxan",
        "moods": ['Conversational']
    },
    "Louis": {
        "voice_id": "fr-FR-louis",
        "moods": ['Promo', 'Conversational']
    },
    "Jong-su": {
        "voice_id": "ko-KR-jong-su",
        "moods": ['Conversational']
    },
    "Harper": {
        "voice_id": "en-AU-harper",
        "moods": ['Conversational', 'Casual']
    },
    "Ruby": {
        "voice_id": "en-UK-ruby",
        "moods": ['Conversational', 'Promo', 'Angry', 'Sad', 'Newscast', 'Calm']
    },
    "Kimi": {
        "voice_id": "ja-JP-kimi",
        "moods": ['Conversational']
    },
    "Ken": {
        "voice_id": "en-US-ken",
        "moods": ['Conversational', 'Promo', 'Newscast', 'Storytelling', 'Calm', 'Furious', 'Angry', 'Sobbing', 'Sad', 'Wizard', 'Audiobook']
    },
    "Silvio": {
        "voice_id": "pt-BR-silvio",
        "moods": ['Conversational']
    },
    "Mani": {
        "voice_id": "ta-IN-mani",
        "moods": ['Conversational']
    },
    "Ralf": {
        "voice_id": "de-DE-ralf",
        "moods": ['Conversational']
    },
    "Jaxon": {
        "voice_id": "en-UK-jaxon",
        "moods": ['Conversational']
    },
    "River": {
        "voice_id": "en-US-river",
        "moods": ['Conversational']
    },
    "Priya": {
        "voice_id": "en-IN-priya",
        "moods": ['Conversational']
    },
    "Theo": {
        "voice_id": "en-UK-theo",
        "moods": ['Narration', 'Promo', 'Calm', 'Sad', 'Angry']
    },
    "Katie": {
        "voice_id": "en-UK-katie",
        "moods": ['Conversational']
    },
    "Jacek": {
        "voice_id": "pl-PL-jacek",
        "moods": ['Conversational']
    },
    "Lorenzo": {
        "voice_id": "it-IT-lorenzo",
        "moods": ['Conversational', 'Promo']
    },
    "Maverick": {
        "voice_id": "en-US-maverick",
        "moods": ['Narration']
    },
    "Shaan": {
        "voice_id": "hi-IN-shaan",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Amara": {
        "voice_id": "en-US-amara",
        "moods": ['Conversational', 'Narration']
    },
    "Mason": {
        "voice_id": "en-UK-mason",
        "moods": ['Documentary']
    },
    "Surya": {
        "voice_id": "en-IN-surya",
        "moods": ['Documentary']
    },
    "Tao": {
        "voice_id": "zh-CN-tao",
        "moods": ['Conversational', 'Promo', 'Calm', 'Sad']
    },
    "Molly": {
        "voice_id": "en-US-molly",
        "moods": ['Conversational']
    }
}

# flet interface
def main(page: ft.Page):
    page.title = "MurfTone"
    page.padding = 20
    page.bgcolor = "#1A1B26"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 800
    page.window_height = 600
    page.window_resizable = True
    page.window_center = True
    page.scroll = ft.ScrollMode.AUTO
    page.adaptive = True

    # Create the UI Widgets
    title = ft.Text(
        "MurfTone",
        size=36,
        weight=ft.FontWeight.BOLD,
        color="#BB9AF7",
        text_align=ft.TextAlign.CENTER,
        scale=ft.transform.Scale(scale=0.8),
        animate_scale=ft.animation.Animation(1000, ft.AnimationCurve.BOUNCE_OUT)
    )

    subtitle = ft.Text(
        "AI Voice Generator",
        size=14,
        color="#A9B1D6",
        text_align=ft.TextAlign.CENTER,
        opacity=0,
        animate_opacity=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    text_input = ft.TextField(
        label="Enter your text here...",
        width=page.window_width - 100,
        height=100,
        multiline=True,
        max_lines=4,
        bgcolor="#24283B",
        color="#A9B1D6",
        border_radius=15,
        border_color="#BB9AF7",
        focused_border_color="#7AA2F7",
        prefix_icon=ft.Icons.TEXT_FIELDS,
        offset=ft.transform.Offset(-0.5, 0),
        animate_offset=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    # voice selection
    voice_selection = ft.Dropdown(
        label="Choose Voice",
        options=[ft.dropdown.Option(voice) for voice in VOICE_MOODS.keys()],
        width=page.window_width - 100,
        bgcolor="#24283B",
        color="#A9B1D6",
        border_radius=15,
        border_color="#BB9AF7",
        focused_border_color="#7AA2F7",
        value="Samantha",
        offset=ft.transform.Offset(-0.5, 0),
        animate_offset=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    # mood selection
    mood_selection = ft.Dropdown(
        label="Choose Mood",
        width=page.window_width - 100,
        bgcolor="#24283B",
        color="#A9B1D6",
        border_radius=15,
        border_color="#BB9AF7",
        focused_border_color="#7AA2F7",
        offset=ft.transform.Offset(-0.5, 0),
        animate_offset=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    # Create rows with icons and dropdowns
    voice_row = ft.Row(
        controls=[
            ft.Icon(ft.Icons.RECORD_VOICE_OVER, color="#A9B1D6"),
            voice_selection
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    mood_row = ft.Row(
        controls=[
            ft.Icon(ft.Icons.MOOD, color="#A9B1D6"),
            mood_selection
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=10
    )

    def update_moods(e=None):
        selected_voice = voice_selection.value
        mood_selection.options = [
            ft.dropdown.Option(mood) for mood in VOICE_MOODS.get(selected_voice, {}).get("moods", [])
        ]
        mood_selection.value = mood_selection.options[0].text if mood_selection.options else None
        page.update()

    voice_selection.on_change = update_moods
    update_moods()

    voice_speed = ft.Slider(
        min=-30,
        max=30,
        value=0,
        divisions=10,
        label="{value}%",
        active_color="#BB9AF7",
        inactive_color="#414868",
        thumb_color="#7AA2F7",
        offset=ft.transform.Offset(-0.5, 0),
        animate_offset=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    # Volume control
    volume_slider = ft.Slider(
        min=0,
        max=100,
        value=50,
        divisions=10,
        label="{value}%",
        active_color="#BB9AF7",
        inactive_color="#414868",
        thumb_color="#7AA2F7",
        offset=ft.transform.Offset(-0.5, 0),
        animate_offset=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    # Generate Ai voice
    def generate_audio():
        selected_voice = voice_selection.value
        voice_id = VOICE_MOODS.get(selected_voice,{}).get("voice_id")

        if not text_input.value.strip():
            print("Error, you need some text....")
            return None
        try:
            response = client.text_to_speech.generate(
                format="MP3",
                sample_rate=48000.0,
                channel_type="STEREO",
                text=text_input.value,
                voice_id=voice_id,
                style=mood_selection.value,
                pitch=voice_speed.value
            )
            return response.audio_file if hasattr(response, "audio_file") else None
        except Exception as e:
            print (f"Error: {e}")
            return None
        
    def save_and_play(e):
        audio_url = generate_audio()
        if not audio_url:
            print("Error: no audio found...")
            return
        
        try:
            response = requests.get(audio_url, stream=True)
            if response.status_code == 200:
                file_path = os.path.abspath("audio.mp3")
                
                # Clear any existing audio players
                page.overlay.clear()
                page.update()
                
                # Try to remove existing file if it exists
                try:
                    if os.path.exists(file_path):
                        os.remove(file_path)
                except:
                    pass
                
                # Save the new audio file
                with open(file_path, "wb") as file:
                    for chunk in response.iter_content(chunk_size=1024):
                        file.write(chunk)

                print("Audio Saved As:", file_path)
                audio_player = fta.Audio(
                    src=file_path,
                    autoplay=True,
                    volume=volume_slider.value / 100
                )
                page.overlay.append(audio_player)
                page.update()
            else:
                print("Failed to get audio")
        except Exception as e:
            print("ERROR", e)

    # enter button
    btn_enter = ft.ElevatedButton(
        "Generate Voice",
        bgcolor="#BB9AF7",
        color="#1A1B26",
        width=page.window_width - 100,
        height=50,
        on_click=save_and_play,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            elevation=5,
            animation_duration=300
        ),
        scale=ft.transform.Scale(scale=0.95),
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE_OUT)
    )

    # Build a UI Container
    input_container = ft.Container(
        content=ft.Column(
            controls=[
                text_input,
                ft.Divider(color="#414868", height=20),
                voice_row,
                ft.Divider(color="#414868", height=20),
                mood_row,
                ft.Divider(color="#414868", height=20),
                ft.Text("Adjust Pitch", size=18, weight=ft.FontWeight.BOLD, color="#BB9AF7"),
                voice_speed,
                ft.Divider(color="#414868", height=20),
                ft.Text("Adjust Volume", size=18, weight=ft.FontWeight.BOLD, color="#BB9AF7"),
                volume_slider,
                ft.Divider(color="#414868", height=20),
                btn_enter
            ],
            spacing=15,
            alignment=ft.MainAxisAlignment.CENTER
        ),
        padding=20,
        border_radius=20,
        bgcolor="#24283B",
        shadow=ft.BoxShadow(blur_radius=12, spread_radius=2, color="#BB9AF7"),
        animate=ft.animation.Animation(1000, ft.AnimationCurve.EASE_OUT)
    )

    def animate_ui(e):
        title.scale = 1.0
        subtitle.opacity = 1
        text_input.offset = ft.transform.Offset(0, 0)
        voice_selection.offset = ft.transform.Offset(0, 0)
        mood_selection.offset = ft.transform.Offset(0, 0)
        voice_speed.offset = ft.transform.Offset(0, 0)
        volume_slider.offset = ft.transform.Offset(0, 0)
        page.update()

    def delayed_animation():
        animate_ui(None)

    page.add(
        ft.Column(
            controls=[
                title,
                subtitle,
                ft.Divider(color="#414868", height=30),
                input_container
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
    
    # Start animations
    page.run_thread(delayed_animation)
    page.update()


# Run the App
if __name__=="__main__":
    ft.app(target=main, assets_dir=".")