import os
import json
import sys

# HOW TO USE:
# You can pass the Fiction Name as an argument:
# python generate_audio_json.py MyFiction
# If you forget:
# python generate_audio_json.py
#  You'll get the prompt: "Enter FictionName:"

# Define common audio file extensions
AUDIO_EXTENSIONS = ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma', '.aiff']

def is_audio_file(filename):
    return any(filename.lower().endswith(ext) for ext in AUDIO_EXTENSIONS)

def main():
    # Get FictionName from command-line or ask user
    if len(sys.argv) < 2:
        fiction_name = input("Enter FictionName: ")
    else:
        fiction_name = sys.argv[1]

    # List audio files in current directory
    audio_files = [f for f in os.listdir('.') if os.path.isfile(f) and is_audio_file(f)]

    # Create room entries
    rooms = [
        {"name": os.path.splitext(f)[0], "audio_path": f"user://{f}"}
        for f in audio_files
    ]

    # Compose final JSON structure
    data = {
        "FictionName": fiction_name,
        "Rooms": rooms
    }

    # Write to file
    with open("audio_files.json", "w", encoding="utf-8") as out_file:
        json.dump(data, out_file, indent=4)

    print("✅ audio_files.json created successfully.")

if __name__ == "__main__":
    main()

