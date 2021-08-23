#!/usr/bin/env python
# coding: utf-8

# generate protein sequence (.fasta) for chimera from two fasta files
import sys
import getopt
import os

# generate chimera protein sequences
def chimera(input_directory,output_directory,fasta_1,fasta_2,aa,bb,linker,length):
    f_1 = open(input_directory+fasta_1,"r")
    f_2 = open(input_directory+fasta_2,"r")
    lines_1 = f_1.readlines()
    lines_2 = f_2.readlines()
    f_1_name = ''
    f_2_name = ''
    f_1_seq = ''
    f_2_seq = ''
    for line in lines_1:
        if line[0] == '>':
            f_1_name = (line[1:].split(' ')[0][:-1])
        else:
            f_1_seq = f_1_seq + line[:-1]
    for line in lines_2:
        if line[0] == '>':
            f_2_name = (line[1:].split(' ')[0][:-1])
        else:
            f_2_seq = f_2_seq + line[:-1]
    # generate sequence of chimera 
    if aa == 'f' and bb == 'f':
        c = f_1_seq+linker*int(length)+f_2_seq
    elif aa == 'f' and bb != 'f':
        l_2 = bb.split(',')
        c = f_1_seq+linker*int(length)+f_2_seq[(int(l_2[0])-1):(int(l_2[1]))]
    elif aa != 'f' and bb == 'f':
        l_1 = aa.split(',')
        c = f_1_seq[(int(l_1[0])-1):(int(l_1[1]))]+linker*int(length)+f_2_seq
    else:
        l_1 = aa.split(',')
        l_2 = bb.split(',')
        c = f_1_seq[(int(l_1[0])-1):(int(l_1[1]))]+linker*int(length)+f_2_seq[(int(l_2[0])-1):(int(l_2[1]))]
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
    aa = '' # the region for fasta_1
    bb = '' # the region for fasta_2
    linker = '' # linker 
    length = '' # repeat times of linker
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:a:b:c:d:l:n:")
    except getopt.GetoptError:
        print('python chimera_generation.py -i <> -o <> -a <> -b <> -c <> -d <> -l <> -n <>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('This script can generate protein sequence (.fasta) for chimera from two fasta files.')
            print('command: python chimera_generation.py -i <> -o <> -a <> -b <> -c <> -d <> -l <> -n <>')
            print('-i: input directory;')
            print('-o: output directory;')
            print('-a: the fasta file of the first protein;')
            print('-b: the fasta file of the second protein;')
            print('-c: the start and end for the first protein;')
            print('-d: the start and end for the second protein;')
            print('-c & -d: s for start, e for end, f for full length, example: (1) s,e (2) f;')
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
        elif opt == "-c":
            aa = arg
        elif opt == "-d":
            bb = arg
        elif opt == "-l":
            linker = arg
        elif opt == "-n":
            length = arg
            
    # generate chimera protein sequences
    chimera(input_directory,output_directory,fasta_1,fasta_2,aa,bb,linker,length)
    
if __name__ == "__main__":
    main(sys.argv[1:])






