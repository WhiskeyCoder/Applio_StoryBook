import os
import shutil
from gradio_client import Client
from datetime import datetime
from pydub import AudioSegment


names_and_files = {
    "Narrator": [r"path\to\narrator\file.pth", r"path\to\narrator\file.index", "en-US-NarratorVoice"],
    "Kim": [r"path\to\kim\file.pth", r"path\to\kim\file.index", "en-US-KimVoice"],
}


def ensure_output_folder(folder_name):
    try:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
        print(f"Folder '{folder_name}' is ready for use.")
    except Exception as e:
        print(f"Error creating folder '{folder_name}': {e}")
    return folder_name


audio_file_count = {}


def convert_and_save_audio(name, text, output_folder, chunk_num):
    pth_file, index_file, tts_voice = names_and_files[name]
    client = Client("http://127.0.0.1:6969/")
    if name not in audio_file_count:
        audio_file_count[name] = 1
    else:
        audio_file_count[name] += 1

    filename = f"{chunk_num}_{name}_chunk.mp3"
    output_path = os.path.join(output_folder, filename)
    result = client.predict(
        text,
        tts_voice,
        0, 3, 0.75, 128, "rmvpe",
        output_path, output_path,
        pth_file, index_file,
        api_name="/run_tts_script"
    )

    if result:
        print(f"Audio for {name} saved successfully as {filename}.")
    else:
        print(f"Error generating audio for {name}.")


def process_script(filename):
    output_folder = ensure_output_folder("output_audio")
    try:
        with open(filename, 'r') as script_file:
            chunk_num = 1
            for line in script_file:
                if ": " in line:
                    name, text = line.split(": ", 1)
                    if name.strip() in names_and_files:
                        convert_and_save_audio(name.strip(), text.strip(), output_folder, chunk_num)
                        chunk_num += 1
                    else:
                        print(f"Name '{name.strip()}' not found in dataset.")
    except FileNotFoundError:
        print(f"File {filename} not found.")



def combine_audio_files(folder_path, output_filename="combined_audio.mp3"):
    ensure_output_folder(folder_path)
    files = [f for f in os.listdir(folder_path) if f.endswith(".mp3")]
    sorted_files = sorted(files, key=lambda x: int(x.split("_")[0]))
    combined = AudioSegment.empty()
    for filename in sorted_files:
        print(f"Processing {filename}...")
        file_path = os.path.join(folder_path, filename)
        try:
            audio_segment = AudioSegment.from_mp3(file_path)
            combined += audio_segment
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    output_path = os.path.join(folder_path, output_filename)
    combined.export(output_path, format="mp3", bitrate="192k")
    print(f"Combined audio saved to {output_path}")


if __name__ == "__main__":
    script_filename = "script.txt"
    output_folder = "output_audio"
    process_script(script_filename)
    combine_audio_files(output_folder)
