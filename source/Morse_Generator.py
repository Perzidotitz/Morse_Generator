import Morse_Characters as mc
import Morse_Translater as mt
import numpy as np 
from scipy.io import wavfile as wf

def morse_generator(input, p_csv, p_output):
    """Generate a wav file containing the morse code

    Args:
        input (str): The input to be translated
        p_csv (str): path to morse<-->latin correspondancy csv
        p_output (str): path to store the output
    """
    rate = 44100
    mt_translater = mt.Morse_Translater(input, p_csv)
    mt_translater.translate()
    
    code = mt_translater.code
    final_signal = []

    for c in code:
        c.generate_signal()
        audio_signal = c.signal
        final_signal.append(audio_signal)
            
    np_final_signal = np.hstack(final_signal)
    wf.write(p_output, rate, np_final_signal)
    
