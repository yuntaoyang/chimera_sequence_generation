#!/usr/bin/env python
# coding: utf-8

# generate protein sequence (.fasta) for chimera from two fasta files
import sys
import getopt
import os

# generate chimera protein sequences
def chimera(input_directory,output_directory,fasta_1,fasta_2,linker,length):
    f_1 = open(input_directory+fasta_1,"r")
    f_2 = open(input_directory+fasta_2,"r")
    lines_1 = f_1.readlines()
    lines_2 = f_2.readlines()
    for n,line in enumerate(lines_1):
        if line[0] == '>':
            f_1_name = (line[1:].split(' ')[0][:-1])
        if line == '\n':
            f_1_seq = lines_1[n-1][:-1]
    for n,line in enumerate(lines_2):
        if line[0] == '>':
            f_2_name = (line[1:].split(' ')[0][:-1])
        if line == '\n':
            f_2_seq = lines_2[n-1][:-1]
    c = f_1_seq+linker*int(length)+f_2_seq # generate sequence of chimera      
    file_name = f_1_name+'_'+f_2_name+'_'+linker+'_'+str(length) # set up file name 
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)
    f = open(output_directory+file_name+'.fasta','w') # generate fasta file
    f.writelines('>'+file_name+'\n') # first line of fasta file: chimera name
    f.writelines(c+'\n') # lines for chimera sequences
    f.close()

# main function
def main(argv):
    input_directory = '' # input directory
    output_directory = '' # output directory
    fasta_1 = '' # the fasta file of the first protein
    fasta_2 = '' # the fasta file of the second protein
    linker = '' # linker 
    length = '' # repeat times of linker
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:a:b:l:n:")
    except getopt.GetoptError:
        print('python sequence_generation.py -i <> -o <> -a <> -b <> -l <> -n <>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('This script can generate protein sequence (.fasta) for chimera from two fasta files.')
            print('command: python sequence_generation.py -i <> -o <> -a <> -b <> -l <> -n <>')
            print('-i: input directory;')
            print('-o: output directory;')
            print('-a: the fasta file of the first protein;')
            print('-b: the fasta file of the second protein;')
            print('-l: GGGGS or G;')
            print('-n: repeat times of linker;')
            sys.exit()
        elif opt == "-i":
            input_directory = arg
        elif opt == "-o":
            output_directory = arg
        elif opt == "-a":
            fasta_1 = arg
        elif opt == "-b":
            fasta_2 = arg
        elif opt == "-l":
            linker = arg
        elif opt == "-n":
            length = arg
            
    # generate chimera protein sequences
    chimera(input_directory,output_directory,fasta_1,fasta_2,linker,length)
    
if __name__ == "__main__":
    main(sys.argv[1:])






