# Data Formats
# https://rosalind.info/problems/frmt/

from Bio import Entrez, SeqIO
Entrez.email = "your_name@your_mail_server.com"
handle = Entrez.efetch(db="nucleotide", id=["JQ712982 NM_002133 NM_001082732 JX317624 JX308817 NR_073358 JQ712977 JQ712981 NM_002037"], rettype="fasta")

records = list(SeqIO.parse(handle, "fasta"))
lens = [len(r.seq) for r in records]
print(records[lens.index(min(lens))].format("fasta"))
