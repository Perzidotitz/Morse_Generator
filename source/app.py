import Morse_Generator as mg

input = "Hi Empenn ! Where do you eat today ? :knife_fork_plate: Supélec :bento: IRISA :green_salad: Biocoop :hospital: CHU :wave: not with the team"
p_csv = "morse.csv"
p_output = "output/output.wav"

mg.morse_generator(input, p_csv, p_output)