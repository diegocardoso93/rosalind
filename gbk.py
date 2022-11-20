# GenBank Introduction
# https://rosalind.info/problems/gbk/

from Bio import Entrez
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.esearch(db="nucleotide", term='"Zea mays"[Organism] AND rbcL[Gene]')
record = Entrez.read(handle)
print(record["Count"])

handle = Entrez.esearch(db="nucleotide", term='"Anthoxanthum"[Organism] AND 2003/7/25:2005/12/27[Publication Date]')
record = Entrez.read(handle)
print(record["Count"])

handle = Entrez.esearch(db="nucleotide", term='"Psiloglonium"[Organism] AND 2003/09/11:2010/11/01[Publication Date]')
record = Entrez.read(handle)
print(record["Count"])
