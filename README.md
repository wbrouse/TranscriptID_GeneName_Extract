# TranscriptID_GeneName_Extract

This script pulls the transcript ID and gene names from multi-fasta file headers. The outputs are used by a separate script to organize data into gene named directories containing all associated transcripts

The script requires only one file to run, the input fasta file containing multiple fastas within itself.

To run the script, call python, then script name, then input fasta name. Output will be a T2G.txt file and an off.txt file. These files can be used by a separate script to organize all transcript into their respective gene named directories
