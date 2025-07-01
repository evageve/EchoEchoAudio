import os
import json
import sys

# HOW TO USE:
# You can pass the Fiction Name as an argument (inside the json and for the json filename) :
# python generate_audio_json.py MyFiction
# If you forget:
# python generate_audio_json.py
#  You'll get the prompt: "Enter FictionName:"

# Common audio file extensions
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma', '.aiff']

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in AUDIO_EXTENSIONS)

def main():
    # Get FictionName from command-line or prompt
    if len(sys.argv) < 2:
        fiction_name = input("Enter FictionName: ")
    else:
        fiction_name = sys.argv[1]

    # Find audio files in current directory
    audio_files = [f for f in os.listdir('.') if os.path.isfile(f) and is_audio_file(f)]

    # Prepare room entries
    rooms = [
        {"name": os.path.splitext(f)[0], "audio_path": f"user://{f}"}
        for f in audio_files
    ]

    # Build JSON data
    data = {
        "FictionName": fiction_name,
        "Rooms": rooms
    }

    # Output filename based on FictionName
    output_filename = f"{fiction_name}.json"

    # Write JSON
    with open(output_filename, "w", encoding="utf-8") as out_file:
        json.dump(data, out_file, indent=4)

    print(f"✅ {output_filename} created successfully.")

if __name__ == "__main__":
    main()

