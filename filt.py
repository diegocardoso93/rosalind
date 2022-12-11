# Read Filtration by Quality
# https://rosalind.info/problems/filt/

from Bio import SeqIO
import io

fasta_str = """@Rosalind_0049_1
GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
+
FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
@Rosalind_0049_2
AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
+
1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
@Rosalind_0049_3
ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
+
B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+
"""

records = list(SeqIO.parse(io.StringIO(fasta_str), "fastq"))

count = 0
threshold = 20
percentage = 0.9
for record in records:
    quality = record.letter_annotations["phred_quality"]
    passes = 0
    for q in quality:
        if q >= threshold:
            passes += 1
    if passes/len(quality) >= percentage:
        count += 1
print(count)
