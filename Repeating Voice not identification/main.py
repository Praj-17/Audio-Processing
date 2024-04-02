from src import SilenceSplitter
from src import TrascribeSRT
from src import Similairty_checker

splitter = SilenceSplitter()
transcriber = TrascribeSRT()
checker = Similairty_checker()



if __name__ == "__main__":
    mp3_path = "output2.mp3"


    # step 1 split the audio on silence
    folder_path = splitter.split_on_silence(mp3_path=mp3_path)

    #Step 2 Transcribe The text
    results = transcriber.transcribe_folder(folder_path)

    # Get All text a   list  of strings

    texts = [i['text'] for i in results]

    check = checker.are_strings_similar(texts)

    if check:
        print("Strings are similiar")
    else:
        print("Strings are not similar")




