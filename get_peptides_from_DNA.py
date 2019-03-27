import sys
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC


def translation(messenger_rna):
    global peptides
    peptides = []
    start = messenger_rna.find('AUG')
    if messenger_rna.find('AUG') != -1:
        peptide = messenger_rna[start:].translate(to_stop=True)
        peptides.append(peptide)
        mito_translation(messenger_rna)


def mito_translation(messenger_rna):
    start = messenger_rna.find('AUG')
    alt_start = messenger_rna.find('AUA')
    if messenger_rna.find('AUG') != -1:
        mito_peptide = messenger_rna[start:].translate(table=2, to_stop=True)
        peptides.append(mito_peptide)
    elif messenger_rna.find('AUA') != -1:
        mito_peptide2 = messenger_rna[alt_start:].translate(table=2, to_stop=True)
        peptides.append(mito_peptide2)
    peptides_list = sorted(peptides, key=len)
    for peptide in peptides_list:
        print(peptide)


def transcription(my_seq):
    messenger_rna = my_seq.transcribe()

    translation(messenger_rna)


def main():
    if len(sys.argv) < 2:
        print('Use like this: get_peptides_from_DNA.py <sequence> ')
        exit()
    my_seq = Seq(sys.argv[1], IUPAC.unambiguous_dna)

    transcription(my_seq)


if __name__ == '__main__':
    main()
