# Audio Storytelling Project with Applio and PyDub

This project leverages the power of the Applio text-to-speech (TTS) engine, with RVC models and the PyDub library to create audio stories by combining character-specific voiceovers. The script processes a given screenplay, matches lines to characters, and generates audio segments using distinct voices for each character. Finally, it combines these segments into a single audio file for playback.

I used Kim Possible as an example, due to it being my favourite tv show as a kid. The sample script.txt is uploaded as well as an audio file to hear it. I warn you, it is not amazing, due and some configurations need to be fixed within my settings on Applio. Here is the sample audio file 

[Kim Possible Sample Audio](https://github.com/WhiskeyCoder/Applio_StoryTeller/blob/main/KimPossible_test_script.mp3)

## Project Overview

The core of this project is a Python script that reads a screenplay from a text file, where each line is attributed to a character or a narrator. For each line, the script uses predefined TTS voices to generate audio segments, ensuring that each character's dialogue is spoken in a unique voice. These segments are then concatenated in order, producing a coherent audio story.

### Features

- **Character-Specific Voiceovers:** Utilize different TTS voices for characters and the narrator to enhance storytelling.
- **Audio File Combination:** Merge multiple audio segments into a single file for seamless story playback.
- **Flexible Script Input:** Process any screenplay formatted with "Character: Dialogue" lines.

## Setup

Before running the project, ensure you have Python installed on your machine and the following dependencies:
- [`Applio`](https://github.com/IAHispano/Applio/releases)
- `pydub`
- `gradio_client` (Custom client for Applio TTS engine)

You can install the necessary libraries using pip:

```bash
pip install pydub
pip install gradio_client  # Or use the appropriate command to install your custom client
```

Additionally, make sure you have the Apollo server running and accessible to accept TTS requests.

## How It Works

1. **Prepare the Screenplay:** Write your screenplay in a text file with each line formatted as `Character: Dialogue`. For example:

    ```
    Narrator: In the dead of night, two figures approach the villain's lair.
    Kim: Look, there's the entrance.
    Ron: I knew that!
    ```

2. **Configure Character Voices:** In the script, map each character to their corresponding TTS voice RVC settings, including the `.pth` and `.index` files for the Apollo engine, and specify the TTS voice ID.

    ```python
    names_and_files = {
        "Narrator": [r"path\to\narrator\file.pth", r"path\to\narrator\file.index", "en-US-NarratorVoice"],
        "Kim": [r"path\to\kim\file.pth", r"path\to\kim\file.index", "en-US-KimVoice"],
        # Add more characters as needed
    }
    ```

3. **Process the Screenplay:** The script reads the screenplay file, generates an audio file for each line using the specified TTS voices, and saves them in an output directory.

4. **Combine Audio Segments:** Using PyDub, the script then combines all generated audio segments into a single file, preserving their order.

5. **Playback the Story:** The final combined audio file is your story, ready to be shared or played back.

## Running the Script

To execute the project:

1. Place your screenplay text file in the project directory.
2. Run the script with Python:

    ```bash
    python your_script_name.py
    ```

3. The script prompts you to input necessary details or automatically processes the screenplay if pre-configured.
4. Find the combined audio file in the specified output directory.

## Customization
You can customize this project by adding more characters that you have RVC models for, adjusting the TTS voices, or modifying the screenplay format. The script is designed to be flexible, allowing for various storytelling styles and preferences.

## Conclusion

This project showcases the potential of combining text-to-speech technology with audio processing libraries to create immersive audio stories. Whether you're a hobbyist looking to bring your stories to life or a developer exploring TTS applications, this project provides a foundation for innovative storytelling techniques. My use case is to create audio for someone with eyesight issues that is close to me so they can enjoy stories and shows.

## Future Plans
- Add prompting for openAI / LMstudio to generate unique stories or create live text-to-speech conversations
- improve the speech settings
- improve the mp3 file combining to make better outputs

---
