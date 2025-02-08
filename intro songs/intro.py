from pydub import AudioSegment

# Load the audio file
audio = AudioSegment.from_mp3("kraftwerk-therobots.mp3")

# Duration of the audio in milliseconds
duration_ms = len(audio)

# Define the length of each segment (4 seconds)
segment_length_ms = 4000

# Function to add fade-in and fade-out effects and make the segment quieter
def process_segment(segment):
    # Fade-in and fade-out (1 second each)
    segment = segment.fade_in(2000).fade_out(2000)
    # Make the segment quieter (reduce volume by 6dB)
    segment = segment - 20
    return segment

# Split and export the segments
for i, start in enumerate(range(0, duration_ms, segment_length_ms)):
    segment = audio[start:start + segment_length_ms]
    processed_segment = process_segment(segment)
    processed_segment.export(f"{i + 1}.mp3", format="mp3")