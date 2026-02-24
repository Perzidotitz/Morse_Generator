import numpy as np 

class Morse_Input:
    
    def __init__(self, dur):
        """Initialize the morse sound.

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
    
    def __init__(self):
        
        dur = 0.1
        super().__init__(dur)
    
    def to_string(self):
        
        return "."

class Morse_Dash(Morse_Input):
    
    def __init__(self):
        
        dur = 0.5
        super().__init__(dur)
    
    def to_string(self):
        
        return "-"

class Morse_Blank():
    
    def __init__(self, type):
        
        self.fs = 44100
        self.type = type
        
        if(type == "sub_carac"):
            self.dur = 0.1
        else:
            self.dur = 1
        
        self.signal = None
    
    def generate_signal(self):
        
        self.signal =  np.zeros(int(self.dur * self.fs))
    
    def to_string(self):
        
        if(self.type == "sub_carac"):
            return ""
        else:
            return " "
