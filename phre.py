# Read Quality Distribution
# https://rosalind.info/problems/phre/

from Bio import SeqIO
import io

fasta_str = """@Rosalind_0041
GGCCGGTCTATTTACGTTCTCACCCGACGTGACGTACGGTCC
+
6.3536354;.151<211/0?::6/-2051)-*"40/.,+%)
@Rosalind_0041
TCGTATGCGTAGCACTTGGTACAGGAAGTGAACATCCAGGAT
+
AH@FGGGJ<GB<<9:GD=D@GG9=?A@DC=;:?>839/4856
@Rosalind_0041
ATTCGGTAATTGGCGTGAATCTGTTCTGACTGATAGAGACAA
+
@DJEJEA?JHJ@8?F?IA3=;8@C95=;=?;>D/:;74792.
"""

records = list(SeqIO.parse(io.StringIO(fasta_str), "fastq"))

count = 0
threshold = 28
for record in records:
    quality = record.letter_annotations["phred_quality"]
    if sum(quality)/len(quality) < threshold:
        count += 1

print(count)
