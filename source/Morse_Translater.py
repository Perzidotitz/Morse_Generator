import pandas as pd
import numpy as np 
import Morse_Characters as mc
import Input_Cleaner as ic

class Morse_Translater():
    
    def __init__(self, input, p_csv):
        """Initialize the translater

        Args:
            input (string): input to translate
            p_csv (string): path to csv morse-latin correspondancy 
        """
        ic_in = ic.Input_Cleaner(input, p_csv)#Cleaning the input to be translated
        self.input = ic_in.clean()
        print("... CLEANED INPUT : ", self.input)
        self.corr = pd.read_csv(p_csv)
        self.code = []
        
        self.blank_sub_carac = mc.Morse_Blank("sub_carac")
        self.blank_carac = mc.Morse_Blank("carac")
        
    def translate(self):
        """Translates an input into a morse code
        """
        
        for c in self.input:
            if(c == " "):
                self.code.append(self.blank_carac) #Doubling the space between words
            else: 
                morse_carac_str = self.corr[self.corr["Latin"] == c.upper()].iloc[0]["Morse"] #getting the Morse translation

                for m in morse_carac_str:

                    if(m == "."):
                        morse_sub_carac = mc.Morse_Dot()
                        self.code.append(morse_sub_carac)
                        self.code.append(self.blank_sub_carac)#Every sub character is followed by a small blank space.
                    elif(m == "-"):
                        morse_sub_carac = mc.Morse_Dash()
                        self.code.append(morse_sub_carac)
                        self.code.append(self.blank_sub_carac)

                self.code.append(self.blank_carac)#And every caracter is followed by a big blank space !  
        print("... MORSE TRANSLATION : ", self.to_string())
            
    def to_string(self):
        """Simple to string function for debugging purposes

        Returns:
            str: the morse code in string
        """
        res = ""
        for carac in self.code:
            res += carac.to_string()
        return res

