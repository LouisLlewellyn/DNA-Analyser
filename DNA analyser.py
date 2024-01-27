# DNA Sequence Analyser

markers = ["ATCG", "TCGA", "CCAT", "ATGA", "GACT", "TCAA", "CGTA", "GGAC", "ATTG"]

patterns = {"CT": "TC", "AG": "GA", "TA": "AT", "GC": "CG"}

traits = { "ATCG" : "Blue eyes",
           "TCGA" : "Green eyes",
           "CCAT" : "Red hair",
           "ATGA" : "Dark hair",
           "GACT" : "Taller than average",
           "TCAA" : "Shorter than average",
           "CGTA" : "Big feet",
           "GGAC" : "Small feet",
           "ATTG" : "Clever",
                }

# Uppercase and replace whitespaces in input
def uniform(sequence):
    '''Uniforms input to all capitals'''
    upper_sequence = sequence.upper()
    space_sequence = upper_sequence.replace(" ","")
    return space_sequence

# Checking for certain charaters  in input
def correct(sequence):
    '''Is the input "A" "C" "G" "T"'''
    if all(char in "ACGT" for char in sequence):
        return sequence
    else:
        print("Sorry, we didn't recognise that input, please try again.\n")
        return None

# Checks for certain patterns and swaps characters when found
def switch(sequence, patterns):
    '''Switches a known pattern around'''
    result_str = ''
    i = 0

    while i < len(sequence) - 1:
        current_pair = sequence[i:i+2]

        if current_pair in patterns:
            result_str += patterns[current_pair]
            i += 2
        else:
            result_str += current_pair[0] + current_pair[1]
            i += 2

    return result_str

# Checks for certain pattern of input and assigns to dictionary
def splitting(sequence, markers):
    '''Recognises certain markers'''
    result_str = ''
    i = 0

    while i < len(sequence) - 3:
        current_four = sequence[i:i+4]

        if current_four in markers:
            return current_four
        else:
            result_str += current_four[0] + current_four[1:3]
            i += 4

# Program
print("=========================================")
print("Welcome to LL's Genetic Sequence Analyser")
print("=========================================\n")

print("Our sequencer only recognises 'A' 'C' 'G' 'T' types.\n")
print("Enter 'exit' at any time to leave sequencer.\n")


while True:
    dna_input = input("Please input the DNA Sequence you would like reading: ")

    if dna_input.upper() == 'EXIT':
        break

    upper_sequence = uniform(dna_input)
    print("--------------------------------------------------------------------------------")
    print(f"\tYour input of '{upper_sequence}' is being looked at.")
    print("--------------------------------------------------------------------------------")

    correct_sequence = correct(upper_sequence)
    if correct_sequence:
        pattern_sequence = switch(correct_sequence, patterns)
        print(f"We've noticed a pattern in your sequence. Your new sequence is: {pattern_sequence}\n")

        has_traits = splitting(pattern_sequence, markers)
        if has_traits in traits:
            print(f"Within your DNA Sequence we can see there is a possibility of the following traits:")
            print(f"\t{traits[has_traits]}")
            break
        else:    
            print("We didn't recognise any traits in your input")
            break



