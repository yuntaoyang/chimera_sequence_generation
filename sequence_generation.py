#!/usr/bin/env python
# coding: utf-8

# generate protein sequence (.fasta) for chimera
import pandas as pd
import sys
import getopt
import os

# generate chimera protein sequences
def chimera(input_directory,output_directory,sequence_preprocessing,protein_file,chimera_file,linker,length):
    protein_list = pd.read_csv(input_directory+protein_file) # list of protein name and refseq_accession
    chimera = pd.read_csv(input_directory+chimera_file) # list of chimera (protein name)
    for i in chimera['chimera']: # for loop for each chimera 
        p = i.split(',') # split chimera into a list [p_1,p_2]
        seq = [] # build a list to store sequence of each protein in a chimera
        for j in p: # for loop each protein in a chimera
            refseq = protein_list[protein_list['protein_name'] == j]['refseq_accession'].tolist()[0] # get refseq_accession for each protein
            fasta = sequence_preprocessing[sequence_preprocessing['refseq_accession']==refseq]['sequence'].tolist()[0] # get fasta sequence for each protein
            seq.append(fasta)
        c = '' # sequence of a chimera 
        for l, k in enumerate(seq):
            c = c+k+linker*int(length)# generate sequence of chimera      
        c = c[:-len(linker*int(length))]
        chunks = [c[i:i+50] for i in range(0, len(c), 50)] # split sequences into chunks (length=50)
        file_name = i.replace(',','_')+'_'+linker+'_'+str(length) # set up file name 
        if not os.path.exists(output_directory):
            os.mkdir(output_directory)
        f = open(output_directory+file_name+'.fasta','w') # generate fasta file
        f.writelines('>'+file_name+'\n') # first line of fasta file: chimera name
        for z in chunks: # lines for chimera sequences
            f.writelines(z+'\n')
        f.close()

# main function
def main(argv):
    # set up parameters
    input_directory = '' # input directory
    output_directory = '' # output directory
    sequence_preprocessing_file = '' # csv file generated by sequence_preprocessing.py
    protein_file = '' # a list of protein name and refseq_accession
    chimera_file = '' # a list of chimera
    linker = '' # linker 
    length = '' # repeat times of linker
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:f:p:c:l:n:")
    except getopt.GetoptError:
        print('python sequence_generation.py -i <> -o <> -f <> -p <> -c <> -l <> -n <>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('This script can generate protein sequence (.fasta) for chimera.')
            print('command: python sequence_generation.py -i <> -o <> -f <> -p <> -c <> -l <> -n <>')
            print('-i: input directory;')
            print('-o: output directory;')
            print('-f: the csv file generated by sequence_preprocessing.py;')
            print('-p: a list of protein names and refseq_accessions (.csv), colnames: protein_name,refseq_accession;')
            print('-c: a list of chimeras (.csv), colnames: chimera, separate protein names by comma;')
            print('-l: GGGGS or G;')
            print('-n: repeat times of linker;')
            sys.exit()
        elif opt == "-i":
            input_directory = arg
        elif opt == "-o":
            output_directory = arg
        elif opt == "-f":
            sequence_preprocessing_file = arg
        elif opt == "-p":
            protein_file = arg
        elif opt == "-c":
            chimera_file = arg
        elif opt == "-l":
            linker = arg
        elif opt == "-n":
            length = arg
            
    # read and preprocessing fasta file
    sequence_preprocessing = pd.read_csv(input_directory+sequence_preprocessing_file)
    # generate chimera protein sequences
    chimera(input_directory,output_directory,sequence_preprocessing,protein_file,chimera_file,linker,length)
    
if __name__ == "__main__":
    main(sys.argv[1:])






