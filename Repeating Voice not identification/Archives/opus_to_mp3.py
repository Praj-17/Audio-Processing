from pydub import AudioSegment

def convert_opus_to_mp3(opus_file, mp3_file):
    # Load the Opus file
    audio = AudioSegment.from_file(opus_file, codec="opus")

    # Export as MP3
    audio.export(mp3_file, format="mp3")

# Replace 'input.opus' and 'output.mp3' with your input and output file paths
convert_opus_to_mp3('demo2.opus', 'output2.mp3')
