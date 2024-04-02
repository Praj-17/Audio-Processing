# Import the AudioSegment class for processing audio and the 
# split_on_silence function for separating out silent chunks.
from typing import Any
from pydub import AudioSegment
from pydub.silence import split_on_silence
import os


class SilenceSplitter:
    def __init__(self) -> None:
        self.export_path = "splits"
    # Define a function to normalize a chunk to a target amplitude.
    def match_target_amplitude(self, aChunk, target_dBFS):
        ''' Normalize given audio chunk '''
        change_in_dBFS = target_dBFS - aChunk.dBFS
        return aChunk.apply_gain(change_in_dBFS)
    def get_file_name_from_path(self, file):
        return (file.split("/")[-1]).split(".")[0]
    def initialize_folder(self, folder_path):
        """
        Check if a folder exists, and create it if it doesn't.

        Args:
        folder_path (str): The path to the folder to check and possibly create.
        """
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created.")
        else:
            print(f"Folder '{folder_path}' already exists.")

# Example usage
# ensure_folder_exists("/path/to/your/folder")

    def split_on_silence(self,mp3_path ):
        # Split track where the silence is 2 seconds or more and get chunks using 
    # the imported function.
        chunks = split_on_silence (
        # Use the loaded audio.
         AudioSegment.from_mp3(mp3_path), 
        # Specify that a silent chunk must be at least 2 seconds or 2000 ms long.
        min_silence_len = 200,
        # Consider a chunk silent if it's quieter than -16 dBFS.
        # (You may want to adjust this parameter.)
        silence_thresh = -45
    )
        
        #Export the chunks now

        output_path =  os.path.join(self.export_path,self.get_file_name_from_path(mp3_path))
        self.initialize_folder(output_path)


        # Process each chunk with your parameters
        for i, chunk in enumerate(chunks):
            # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
            silence_chunk = AudioSegment.silent(duration=500)

            # Add the padding chunk to beginning and end of the entire chunk.
            audio_chunk = silence_chunk + chunk + silence_chunk

            # Normalize the entire chunk.
            normalized_chunk = self.match_target_amplitude(audio_chunk, -20.0)
            normalized_chunk.export(
                os.path.join(output_path ,"chunk{0}.mp3".format(i))
                ,
                bitrate = "192k",
                format = "mp3"
            )
            return output_path

if __name__ == "__main__":
    # Load your audio.
    splitter = SilenceSplitter()
    splitter.split_on_silence("output2.mp3")
 



