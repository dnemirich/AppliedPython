import sys
import re
import numpy as np


nucleotides = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def snp_maker(seq, N):
    if len(seq) < N:
        print("Number of SNPs is greater than sequence length")
        N = len(seq)
    seq_array = np.array(seq, dtype='c')
    sites = np.random.randint(0, len(seq) - 1, size=N)
    substitutions_i = np.random.randint(0, 3, size=N)
    substitutions_c = np.zeros(N, dtype='c')
    for n in nucleotides:
        substitutions_c[substitutions_i == n] = nucleotides[n]
        seq_array[sites] = substitutions_c
    return (b''.join(seq_array)).decode()


def process_file(filename, number):
    print("SEQ_ID  |  MUTATION  |  POSITION-OF-MUTATION")
    with open(filename) as f:
        for line in f:
            line = line.strip()
            seq_id, seq = re.split(r'\s+', line)
            snps = snp_maker(seq, number)

            for snp in snps:
                print(f"{seq_id: <22}{snp[0]: >10}->{snp[1]}\t{snp[2]}")


def main():
    if len(sys.argv) < 3:
        print("Usage: change_fasta.py <path-to-file> <command-with-argument>")
        exit()
    command = sys.argv[2]
    number = re.search(r'(?<=SNP)\d+', command).group()

    filename = sys.argv[1]
    try:
        process_file(filename, number)
    except FileNotFoundError:
        print("This file doesn't exist: {filename}")
        exit()


if __name__ == '__main__':
    main()
