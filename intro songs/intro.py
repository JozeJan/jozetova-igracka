from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_mp3("kraftwerk-therobots.mp3")

# Duration of the audio in milliseconds
duration_ms = len(audio)

# Define the length of each segment (3 seconds)
segment_length_ms = 3000

# Split and export the segments
for i, start in enumerate(range(0, duration_ms, segment_length_ms)):
    segment = audio[start:start + segment_length_ms]
    segment.export(f"{i + 1}.mp3", format="mp3")