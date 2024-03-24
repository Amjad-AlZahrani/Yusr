# take the audio from the file 
# import model as md
# import processAudio as pd
import model as md
import processAudio as pd
from scores import addScore3
def AudioRecord(audio, id1="", id2= ""):
    try:
        # Process the audio
        # prc = pd.Convert_Mp3_To_16K_Wav(r'D:\Audio_project\YusrProject\recorded_audio5.wav')
        # # Get the result from the model
        max_=pd.apply_pitch_shift(audio,n_steps=6.2)
        res = md.DetectSound(r'C:\YusrGP\YusrProject\a.wav')
        score = 0
        if res != id1 and res != id2:
            score += 2
        else:
            score += 0
        addScore3(score)
        print("Result is ",res,"Score: ", score)
    except Exception as e:
        print("An error occurred:", str(e))
# AudioRecord(r'c:\YusrProject\kaf.wav')