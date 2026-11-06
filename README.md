(Genetics calculator for the percentage of C-G and A-T)

        1. About me

Hello, nice to meet you!
You can call me like Pox, and i am a I am a Microbiology 
and Bioanalysis student at the University of Antioquia.

This script is part of my self-directed learning process in 
programming and bioinformatics, as I want to create tools for 
analyzing genetic and molecular sequences.
(So no, this isn't a university assignment; I literally did it because I was bored. haha)

I want to clarify that I've only been learning Python for 3 months, so I don't know much yet.

CODE NOTE: As I am a Spanish speaker still learning software, 
some parts of the code are in both Spanish and English. I apologize 
if you read it and don't understand some things. <3

        2. Script presentation

A bioinformatics tool developed in Python for the rapid analysis of
nucleotide sequences in FASTA format. Its main purpose is to calculate 
the Guanine-Cytosine (GC) to Adenine-Thymine (AT) ratio, an essential 
thermodynamic parameter for hybridization processes, PCR primer design, 
and molecular probe development.

Main features of the script:

A. Dual entry method: Allows both copying and pasting the code into FASTA,
and directly searching the hard drive for the FASTA file (pathlib)

B. Intelligent filtering: Validates file writing by searching for the 
standard header that begins with the character ">"

C. Thermodynamic calculation: Ignores descriptive headers and processes 
only the nucleotide chain to yield the total base count and the exact 
percentages of GC and AT (with a recommended standard of 40% to 60% GC 
for hybridization).

        3. Requirements and technologies

A. Python 3.x
B. Native libraries used (no additional external installations required): pathlib

        4. Instructions for use
    
1, Clone the repository or download the main file to your computer.

2, Run the script from your terminal:
    python genetic_FASTA_gc_at_calculator.py
    
3, Follow the interactive on-screen instructions to select whether 
you want to search for a file on the computer or enter the sequence manually.

Thank you so much for watching this project!!!!
