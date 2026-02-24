import pandas as pd

class Input_Cleaner():

    def __init__(self, input, p_csv ):
        
        self.input = input
        df_corr = pd.read_csv(p_csv)
        self.possible_keys = df_corr["Latin"].unique()
    
    def clean(self):
        """Cleans the input string for the Morse Translater

        Returns:
            : the resulting string
        """
        res = ""
        #TODO : add multilanguage components ?
        
        accent_carac_e = ["é","è","ê"]
        accent_carac_a = ["à"]
        accent_carac_c = ["ç"]
        accent_carac_o = ["ô"]
        
        for c in self.input:
            
            if(c.upper() in self.possible_keys or c==" "):
                res+=c
            elif(c in accent_carac_a):
                res+="a"
            elif(c in accent_carac_c):
                res+="c"
            elif(c in accent_carac_e):
                res+="e"
            elif(c in accent_carac_o):
                res+="o"
            else: 
                res+=" "
        
        return res