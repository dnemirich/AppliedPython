import re

site = re.compile('K(K|R)CGH(L|M|Q|R)')  # active site is from prosite

with open('P28240(ACEA_YEAST).txt', 'r') as file:  # fasta is from uniprot
    fasta = file.read()
    match = re.search(site, fasta)
    print("""Isocitrate lyase (P28240) contains its active site (PS00161) \
starting from %s-th position: %s.""" % (match.start(), match.group()))
