from pydub import AudioSegment
import numpy as np
import plotly.graph_objects as go

def plot_audio_waveform(audio_file):
    # Load the audio file using Pydub
    audio = AudioSegment.from_file(audio_file)

    # Convert audio to numpy array
    audio_array = np.array(audio.get_array_of_samples())

    # Calculate the time axis
    duration = len(audio_array) / audio.frame_rate
    time = np.linspace(0., duration, len(audio_array))

    # Calculate dBFS
    dbfs = 20 * np.log10(np.abs(audio_array) / 32767.0)  # Assuming 16-bit audio
    
    # Create a Plotly figure for the waveform and dBFS
    fig = go.Figure()

    # Plot waveform
    fig.add_trace(go.Scatter(x=time, y=audio_array, mode='lines', name='Waveform'))

    # Plot dBFS
    fig.add_trace(go.Scatter(x=time, y=dbfs, mode='lines', name='dBFS', yaxis='y2'))

    # Customize layout
    fig.update_layout(
        title='Audio Waveform and dBFS',
        xaxis=dict(title='Time (s)'),
        yaxis=dict(title='Amplitude'),
        yaxis2=dict(title='dBFS', overlaying='y', side='right'),
        showlegend=True
    )

    # Show the Plotly figure
    fig.show()


if __name__ == "__main__":
    # Replace 'your_audio_file.mp3' with the path to your audio file
    plot_audio_waveform('output2.mp3')
