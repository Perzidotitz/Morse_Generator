import numpy as np 

class Morse_Input:
    
    def __init__(self, dur):
        """Initialize a morse caracter.

        Args:
            dur (int): Duration of the audio sample in seconds. Each morse character has a fixed duration
        """
        self.dur = dur
        
        self.volume = 2
        self.fs = 44100
        self.frequency = 440
        
        self.signal = np.zeros(int(self.fs * self.dur))
        
    def generate_signal(self):
        """Generates the sinusoidal wave. 
        """
        #TODO : maybe add more sounds ? 
        
        t = np.linspace(0, self.dur, int(self.dur*self.fs))
        self.signal = self.volume * np.sin(2 * np.pi * self.frequency * t)
        
    def to_string(self):
        return ""
    
class Morse_Dot(Morse_Input):
    """Dot caracter in morse.
    """
    def __init__(self):
        
        dur = 0.1
        super().__init__(dur)
    
    def to_string(self):
        
        return "."

class Morse_Dash(Morse_Input):
    """Dash caracter in morse.
    """
    def __init__(self):
        
        dur = 0.5
        super().__init__(dur)
    
    def to_string(self):
        
        return "-"

class Morse_Blank():
    """Blank caracter to differenciate morse symbols - latin letters - words in morse. The duration is related to the type of sequence the blank is ending.
    """
    def __init__(self, type):
        
        self.fs = 44100
        self.type = type
        
        if(type == "sub_carac"):
            self.dur = 0.1
        else:
            self.dur = 1
        
        self.signal = None
    
    def generate_signal(self):
        """Generates an empty signal
        """
        self.signal =  np.zeros(int(self.dur * self.fs))
    
    def to_string(self):
        """Simple to string function for debugging purposes

        Returns:
            str: the res string.
        """
        if(self.type == "sub_carac"):
            return ""
        else:
            return " "
