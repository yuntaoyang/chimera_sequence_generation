#!/usr/bin/env python
# coding: utf-8

# data preprocessing of fasta file from NCBI
import pandas as pd
import sys
import getopt
import os


# read and preprocessing fasta file from NCBI
# return: a dataframe of protein refseq accession and sequence
def fasta_preprocess(fasta):
    f = open(fasta,"r")
    lines = f.readlines()
    list_accession = []
    list_sequence = []
    for line in lines:
        if line[0] == '>':
            list_accession.append(line[1:].split(' ')[0])
            seq = ''
        elif line == '\n':
            list_sequence.append(seq)
        else:
            seq = seq + line[:-1]
    protein_refseq_sequence = pd.DataFrame({'refseq_accession':list_accession,'sequence':list_sequence})
    return(protein_refseq_sequence)

# main function
def main(argv):
    # set up parameters
    input_directory = '' # input directory
    output_file = '' # output filename
    fasta_file = '' # fasta file of proteins
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:")
    except getopt.GetoptError:
        print('python sequence_preprocessing.py -i <> -o <> -f <>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('This script is for data preprocessing of a fasta file from NCBI.')
            print('input: a fasta file from NCBI;')
            print('output: a csv file with refseq_accession and sequence;')
            print('command: python sequence_preprocessing.py -i <> -o <> -f <>')
            print('-i: input directory;')
            print('-o: output filename;')
            print('-f: fasta file from NCBI;')
            sys.exit()
        elif opt == "-i":
            input_directory = arg
        elif opt == "-o":
            output_file = arg
        elif opt == "-f":
            fasta_file = arg
     # a dataframe of protein accession and sequence
    protein_refseq_sequence = fasta_preprocess(input_directory+fasta_file)
    protein_refseq_sequence.to_csv(input_directory+output_file, index = False)
    
if __name__ == "__main__":
    main(sys.argv[1:])





