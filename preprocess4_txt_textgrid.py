import os
import textgrid
import soundfile as sf
# Tranform info to textgrid file
# Function to get the duration of a WAV file


def get_wav_duration(wav_path):
    data, samplerate = sf.read(wav_path)
    duration = len(data) / samplerate
    return duration


# Directory path where your text and audio files are stored
directory_path = r'C:\Users\ferni\Downloads\jsut'

# Get the list of text files in the directory
text_files = [file for file in os.listdir(
    directory_path) if file.endswith(".txt")]

for text_file in text_files:
    text_file_path = os.path.join(directory_path, text_file)

    # Extract name from text file
    name = os.path.splitext(text_file)[0]

    # Get corresponding WAV file path
    wav_file_path = os.path.join(directory_path, f"{name}.wav")

    # Get maxTime from the duration of the WAV file
    max_time = get_wav_duration(wav_file_path)

    # Create a TextGrid instance
    tg = textgrid.TextGrid(name=name, minTime=0, maxTime=max_time)

    # Create an IntervalTier
    interval_tier = textgrid.IntervalTier(
        name=name, minTime=0, maxTime=max_time)

    # Read text from the text file
    with open(text_file_path, 'r', encoding='utf-8') as text_file:
        text_content = text_file.read().strip()

    # Add an interval to the IntervalTier
    interval_tier.addInterval(textgrid.Interval(0, max_time, text_content))

    # Append the IntervalTier to the TextGrid
    tg.append(interval_tier)

    # Specify the file path
    output_file_path = os.path.join(directory_path, f"{name}.TextGrid")

    # Write the TextGrid to the specified file path
    tg.write(output_file_path)
