# Protein Translation
# https://rosalind.info/problems/ptra/

from Bio.Seq import translate
coding_dna = "ATGGCACAGGAGGGTACCAGTTGGTTCTCTCCCGCAAAGGGGAGCCTGATTGTAAATGCCAACCCTGGCACTTCCTCCTCCCATTGAAAGGGTATCGCGACTGTCGTCCGAACTTATAGGTGTGTTGTTTCGATCAGTCTTGAGGCGGGATCCCCAAAGGTTCTTGCGCCTAGTCATTGAGGCGCTAACATTGTTGTCCAAGACAAAACCTTTAATATAGGTATTCTGCCAAAACGAACCAGGAGCTGATCGGCAGGTTCGGGTCTTGAATCATCTTGTGGTTACATTTACTCCCTGGCATCAGCTATAATTGAAGAGTACCCTCGTGCATACATCCTGACTTTGATTGGTATACAGTCACTATATAGACAAACGGCAAGGAATCAAGCAGATCCCATCTTTTCAAGCCTGCATAAAGAAGTCAGTGCGCATCATCATGTTCGACTGCCCAATGTATTGGCGCCTGGTGGTGAGGCCAGACTGTCACATAGCGACAGCAGTATTGTGGGCACAAAAGCTAGAGGGCAACGGTTTGTGCTGCGTTGTGAGACCATCGCCAACTTTGTGCGTTTAGCTATAAGTTCAGAGCTAATGCAGTTGAGCATTTGCAGAAGCTACTACTGGGCTGTTGACGAAGGGCCGGACCTAGTGGGGCTAGCAATAATACGTCGCAAGCGTCGGGGGTGCGTTTCGAAAGTAGGGGCTAGAAGGGCTTGGCTTTGATCCCTAACGGCAGGGCCGTACTCCGTCCACCCAAATTCCCAGTCTTCGGATCTCTTTGGTATGGACCTGAAAGGTTGCCGCGCTGTATTCCACATGCTAGACAACCCTATTAATTTGACTTCAACACAGAGTACGTCCTCGCCTACGAGGGACAACGTAGGATTGATCTGACGACCTATTCTGTTATCGCCTTTACTCTCTGGCAGTAGCTTAATGACCCGTAGGCCTGCGCCATATCTGACCTTATGAAGAACTATAGCCCTACTGTCGGACCGACTGCGGCTGTTAACCATGATGGTCCTGCCCCACCTGCGTCGGGAGCGTCATACCCGCCAGTGCTTACGAGGCGTGCAGAGTCTGACCTCAACCTACGACTGGACAAAGCGAAAAGAACCGCACATCAGTTGAAATGACGAAAGGGCCGACGCCCTAGACAAGAAAGCGACGCTAGCAGCGTGCCAGGCCACTAAGGGAGTATATGATTGGCGGCTACATGCGCTCCCCAATTACCCGCTTGAGGACGCACAAGATGACGTAGGGCCAGATGCGACCTTGAAATTAGGATCCCCTGGTAAAAAACGGGCCGCGATTTGCAAACACTGAAGGGGGAGAGTCGTTCTGCTGGTTCTACGAGTCCGCGTTGATTGCTTGTGGGAAGACCGGAGATGAACAAATGCAGACATACAACGTACGCTTATAATTTCCGCCAGACCGAAAAGGTGGCGTCCAATTGCTAACCACCCGAGGCGATCCGAATGCATCGAATTCTTACACGTGTTCGAGCGTCGCAAAGTCGATAAACCAAGTCGTAGCAGGTTTCGTGCAAATTGCTGACGGTGAGAAATCTCCAGTTGGTGCTCATGCTCCTCACCAGAGACATTCACTGAGTGTATCAAACAAGCAATTCTAGCATGATTTAAGGGTTGAAAGGGAAACTTCGCTTGTCGGCATGCGCGCGGATGCGTGGGAACTTGGGATCATTCGCGGGCAACTCTAACTTTACTAGTGGTGTACATTCTCGAGGAGTATGGAGCTAAAGCAGCCAATCGGAAATCGTTATCGTTTGGCACATCCCCTAACATCTCTCAAGAAGCCGGGCCCGAAGGGTGCTGACCTGTTGGTGCGGTGGACCGCTCTAACCATTTGGGCGGGTCCTTATTGGTATTCATTTGATGATTCACCAGAGATACCGTTCAGAAGGACAGGAGTCGAGGTTTCTTTTCGCCTGCCATGCTGTTCCGGCTTATCAAGTGCTTGGTGCTTATGATTGAGTCCTCAAGCGCCTGATCATTCTGCTTCCCTGCGAGCCCCTTTGCCATCAGAGTTCGAGTGGCAAGCGGTGATTTGACAGACCGAATAGCTTGGGTCCTTTTTCCGATCAACACGCCTAGGCTCCCTGGTACTCATCTCTTTCGGACATGCTATGAAGTAGTCAACGTCTATACGTGGAACCCTCCTCCCGCGGGCCAATTCAATTTGTCAGTCTCCGGAGGCTTCTTCACGGCAGGCGATGCGCTTTGAACCCGTCATTGAGGCTGCCTATGTATGTGAGAGACTCCCGGCTGGATACTCGAAATTTCCGGGCCGCCTGTAAGTGATGAATCTGTTTTGAACGCTGGGCAAAACGAGAGCAGGCGGTCTACTGATAATCATGAAAGCAATTACCGACCGGGAGTAACAGGGCCGTGGCAATATATGATGTGTGGCCGAGTCTTTCACCCGGTGAATGCGTCACTGAGTACCGATGTAGAGGACCATGCACAACGTTCGAGAATCATTCTACAGGTAGCGGACTTTAGCGTGATATGCCCAGTGGGTGCCATCAGGTCTGGACGCGTTTTCAAGATCTTTATCGAACGAATTCAAGGACGGTTAGATTCAGTATGAAACAAAACTAGTCGCGGAACGCAACAACAAAGAGCACACCTAGTCATACTTCATTCGGCCGTGCGATTCCTACCGGACGACATATTCAGCTTTCTTGACTCGTCAGTGACGGGCGTAAGGTCAGAAGTCAGCACCCACTTGAGCTGCGGTTTGAACCGTCCGTTTAGTCGGAATCTGAGTGGGACAAGTCGCTCGCGTCTGCCAGACGGTGGGTCGTGCACTCGTATGATCCTGTGGTTCTCGAGTAGTGCGAGCAGTCGAGGCCTCCGCGTGGTAACCAAGCACCATCGAGGTCTGGAGCAATCTAACAACAGCCGGCGCCATTTGTTACTCGTTCTAGAGGTGCAGCTCTCGTCTTATGACTTACCAATTCTGAGGTATCGTAAGGTATATGGCCACAGTGGCTGGAGGGTACTGGAAGCGACTCTTTTTCTAGATGAGTCTATCTGGAGAGTCAACGCCCAGACCATACTCGATAGCCATCGCCCCACCGTGAGCGCGTACGCGCTGGGTGAATCTAAACAACACCCAAAATCTTTGAAGACAGCATCAGTCCCGCTTTCCGACCGGACGTCGCCAATCAGTTCACCTTCGAGCTCGGAGAGGTTACTAAATACACACATTGAAATTCGCATTAGTCCTTATGCTGTACTTCAGGACCATCTCTGCACCGAGGGCTCTCTGGATAAGCATAGAGAGGTTTCCAGGCGCTTTGGCGCGGAAAATTTGTACATGCACTCTGTTGTCAGTAAGAGGTCGAAGATGATAGACGTTGTGGTCTCAGCGAGTCAAAACTTGGAAGGCCAGGCAGTAAGAAAGCCCTTGTTTTTCATTCTTATTAAATGTTGACTGAATAACCCAGCGCCACGTTGAGCCACGTTGGGTCCTTCACCAATACATCCGAGGTTGCAACACAAGAGGTTAATAAAAATGGCAATGGCACCTAGCGGGTGAATGGACCACCCTCGTGGAAGAACAATTGTTGCTTTACATTCAAACGCGAAAAAATTTCTATTATCCCATTGATCACCAGCCATACTGCTGTATAAACCTTCACTTAACGGGCAGTTGGAAGTGAAACCGGACTTAGTTATACTAACTCTAGTCTTATGCCTTTCGTCCCAGGCCTACATAAGGTCAACCACGCACCACGGCAGTACTTCGCGTCACCCCACTTATTTTTGACCCCAGCTCAACCCCGACTGCTGACCACGGCAGACAGGACGCCTCGAAAAAGTTGTGGTGGGAAAATCAACCTCCGTACCGCGAGGAATTCGTCCTTTGACACGTTATACTGTGCACTTCCTGGAAATGTATGCACAATCAGACGGTCTGCCAATATCAGAAAGAGCCGAGCCCGTTATACCAGTTCCGCTTATAATGTTCCGCGTAAGACTTCGCACCTCTTTACATAATAGGTACACTCAATGTATTCGGGCGACACTACTTACACAGGCCGGGCGCGGTAAGACACGTCGTATACACCAAACACCTGTCCCAAACTTCGTACTGTGTGTCGCTATGTCTGTACGGGAGGTCATATCATGTGTAGGGTGGCTTTCAATTTCAATAGCGGTCCATCAAATTTATGGAAATGAGAAGCTTGGTCTTGATGAAGTGTGCGTGCATCCTACCGCCGAGTTTCCCTACGTTGGTTGGGCCGTCCTTTTTGTCTTAAATAGAATATATACTGCCTATCCCAGCCTCAAGGATATGCATATAAACACGTACCTATTACGGATATGCTCAACGTTGACTGTGAACGGCTTAACCTGGGTGCACGTGCAAGACCCACTTTCGGGGAAATTACTTCTAGGTGTAAACACGATATTTCCGATGCGTTCGATCGTCCAACAAAGGGCCACGATAAGCAGTACCGGGAAAAAGGCTCCGATAGCGCCCCCATCGCGGCCTAGCAAGTGGGAACTTTTCCGCAAGCGGCGCGAGGTCTATCCCATTGGTTACCGCCTGAGTAGTCACCCGATATGTCGACATGTGCGCATGTGTTCATTAGAACGGAGTGGCGCTGCCCACCATCAACCCGGCCTGTTATCAATGTTAGTAGTCCACGGCAGCTACACCAGCGTATGGCGGACAATGATGGGCTATGTCGAAGTACCCAAATCAAATACGAGCTTGTCACGGACGGGAGTCCCGAGCTTTAGCAGTAAACGTAAAGATATCCGCACAAAGGATGTAAAGGTATGGATCCCCATGTCTAGGGCTGGACATGCGTCGAGGAACGCGTGTTATTTTAGGAAACCGAGTCAGAGATGCAGATATTTAACCAGTGCGTTCAAGTCACCGTCCTGGGCTGGGAACCACAGGCCTAACAGCATGTGAAGGACTATTCCTTCATTTAGCCTAACGTTAAATCCGAATGGTTCGCCTGCAGGATTTTGCGGAGAGGGCTTATTGGAAAGTAAACGGGATCTAAGAATGCGTTTCTTCAAGCCTACTACTCCATCCGGGTGTCTAGTGATGAGCCTTTTGATATATGACGAGAATATGCGAGGCTGCATAGATTGGAGATGTCGCCCCATAACGAGACGATCGTTCCCGCAAGGTCACCTCTTGTTACGTTCTAAGATCATAGACAGCGATTACGAGCGCGCAAACTCAATGTCGAGCGAATCGAAGGGGGTCCGGGTCGACAGATGTGGGCTTCTGCGGTCCGCCTCACTTGGACGGCGTAGCATCCCGCGGTCCTTACAAAAATTGTGTTTGGGGGCTTTAACACATAGGACGATGAAAGCACCCACAGGATGAAAAAGTCTAAAGGATTGTTCCGGAGAAGGACATGCCAGCGGCTCAGTAAGCATACATGATCATAAATTCGATAATGGCGCCCGCCCCAGCCCCAAGGGATTGCTCACTCCAGGGGTGATTGTGAGTCTAATCCGATTATTATTAAGCGTACATCAGGGTTCCTTGGGTTTAGCTCATTCTTTTCCGGGAGCCGCTTGCTGCTGGCTTCAGTCTCGGCTCTTCAGATCTCGTATTATGCTTGCTTCGTGAAGAGGCAGCTGGCATGAGATTGAATGGCCTTGCCTTAGGTCAGACGCGTGACCGCGCTCGTTAGCGTACGCTGGTCATTCAGCGAACTCCAATATTCTTCCGCGGACCTGTAGGTATGCCAAACCCCTCCATATAGCAACGCGAGTTTCTAAAAAGACTTGAGCCCAGGGATACTCAGTTCGGTCCACAGCGTTTATCCTGAGGATGGTCTTGCCTTCAGGATCTCCTAGGCTCTGAAAACTTTGCATTCTATCCGCAATAGAGAGGGACTGGGGAGGCATAGGAATATGCACCCAGTGAGGAACGAACTATACCACCGGGAGTACTAAACTCCGCAGCGGACGTAGGTATATAGAAGGATATTTCCTTTCCTGCTCAAGATCTAGCGAAGTGGTCTTGTTAAATATAATTGGCACCAACGGCAGGTGACGCAAACCAACTGACCGCTCCCACGGAGGCTCTGCATCCAAGGATTGTTTCGCAGAAACGGTCGCCCTGGATATACAGTTGTTTGCGCCACATAGGCCCCGAATGTTCAATAGGTCACGGACCACAGCGTCGAACAGCCGCTTCAAGCACTATGCATACGGTACAGGCCCACATGCATACTTCCAGGGACACCTCACCGCAAGTCTGGCTACATCCTGTGGGCCTAAAGTGACCTTGCGTCACTATAAAGGGAGACTCTATTTTCCTCCGAGTCTAGGCGGGACACAAGGGGATCTCAATGCTATCAGCGTCCTGTTTATGCAGTCTCTCGCTGGCGAACCCCCCCGACCCTGGCGCACGCCCCGTCAACAGAAAATCGAAAGGTGACACCTCCGGCTCGATCTCAAAGGTTCAACTCATGCCCAAAAGGATGGGTATTACGGGTGGTCCCTAATCCTTACTACAGCTGGGCCTTCGAGGGTGGCACTCCGCGGCAGACATTGTACTTCCAATGGCTTCTATGGTGGCAATGCGCTATGCATATATCTCATTCTATTTCCCGTATTATCGCCGGATGTTTGTAATTGTGGAATACATCTATCTCCACCCACTCTGCTGAATGGGGTATTACGGGGTTATGTGGTGGACGTCTTATCTCGACCGGCATGAGTCTGGTGTTGTAGGGACCCAGATCCGCGAAATCACCCTAGCCAGATTGGGCCGGAGTTTGGTCTAGGTTTCCTACACGGGCGTCCATTCAGGACGCATCACCACACTACAACAGCTTGTTGAGAAGGTCAAGGACCTTGCAGCGAATATAAAACCCAATTTACGTGCCGGTTACGTGGAGCTCTTCTTATTGTATCTGGGCGAATGCCCAGTCAGCTGTGCGGCTGCTTTGAGCACCCTTCCTACATTCCAGCACCCGTACTGCAATCGCAGTGGTTATGTGCTGGGACCGCTTGAGGTGTTCGACCGTCACTCTGAAGTTGCGTTGCGCACTTTACAGGCTTAACCCCAACAACTAAACTCTTGCCGACTCTGTGTGTCGGCGTAGATACGGATGTTAAGCGGAAAATTATGCAAAGTCTTTGGGGGTATCGTTCAAAGGGGCGACTTCTGCGACTGTGGCCTACGTGGCTGACACACGTTCCCAAAGGGAACTTCCGGAATGGGTCGTTGAGCTCCATCTCAGTGGTGGCTACCGATATTGCGATCTTGTTCGTAGTGATGAGTCTTAAACTCTCCCTTTTTAGCGGGATGAGAAACTTCGCGAGAAGTGAGACTTTTCATGATTATTGTGTAGTTCCTTTTGCGATTCTCGGGGCCGGGGGTTTAATACAATATTGCTGGCGACAGTCGCTTTTTCCGACGGCCATGATGCCGCGCTTTTATGAAGAGGTAGCAGTGACCTTTACTGGTTGGGCTGATTCTCGAGATACAGTGCTTGTGAAAGACTTGTCGTCGATCCCTGTAGAATGTCGATCCGCTTATAGCGTCACTCTACCGGGGATCGGCAAATGGAGGGCATATCTAGGTCGGCCGCTTCCGACTTGTTGTGCCTTTAGATGAAGTAATCAAACATATTGCGGCCTACGAGTCCAGATAGATGTGTATCTAAGGTCTGGGATGACAGAGACTGTAGTGCGCGTACATATGTGTTGCCGTCGAGCAATTCTTGCTTTGACGGAATGTAGGAACGGTGTCCGGCAGGCGAAATGCCCGGGCATAATGGAGTTCCATTCAGACGCGGGAGCGTTCAACCTACACGCTTGCTCAGTCTTACTGCGTACCCTTCGTTACGGACCGGTAGAGCTTCCTTCGCTACCGATAGTTATGGTGGAGGGCGAGCCCGCAAGGTCCCCTGGAGCGGTCCGAGTGTGCCGACTCAAGGTCTCATACTTGCAGATCTCATCCCTCCTCCACGCCGGGCTTTCGCATAGCCCTATGCGGCTTAATCACGGTTCCGATTGGTTCGGTCTCTGCTCTCGCATCTTTCGCCATAGACTGTTTCTACTTACTGACAGCATTTCTGACGCGAAGACCCGGCTATATTTTCGTACAGTGCAGTGAGCTAAAAGAAGATTGCCAAAGTGAGCACAGGGTCATGTCTGTTCACCGACCTCCACTACGGGCCCGCGTTGGCAGACTCCGGGCAAACATAAATTACGAATTTCCTTACCTTCTTCTTGCAGACAGCGCTTGTGCCGGCGCAGAAAGTGGGCAATAAGTCCGGATATGGAGACCCTTCGCATGGCAGCGCTGTGGAGCAGCGTACTAACCCAGTTAGGCTTCTGTGACCAATTTAACATTCTAACCTGAATGGGCGGATCGCGCTGGATTTCGCCGGAAAATTTAGACAGTTTGAGGTTACACCAGAGATTTAGTGCTCTATCTACCCCTCTGACGGAGATCATTAGTTTGGGCGAGACATTGTCGAGCGGGCTGTTATGCAGCATACGGGCTAGACGAAGTGACGATGACCAGTCCCGGAACCCGGCAAAAATTCTCGTAGGTGCACCAAGAACATTTGCCCTTGGTTTAGTGACAACTAACACAGGCAAAGTGGGTCACGGATCGCAAACTTGACTGTCACGTTGTGACCTGTTCCCCCGGCCAGGAACGGGGGATCATATATCCGATGTATCTGCGAATTTCGGGGCGGTAAGTGGTTTCTATAGAAAAAACGAGGCTCTGGCGAAGAATTACACCCTAGTCATACAATTCAATGTTCCCGCAGCTCGATGTGACGACCGCATTTGAGTTAAAGAACAAGGATTAAGCTTAACTTGATTCCCCGAATCCTTTCAACACTGACATGTACCCCGGGTGACGCCAAACCATTGTCTGATACGCACAAGGGTACCCTTGCTACGACCATCCCCAACGCCGCATCGAGGTCTATACCAGTGCCACAGGGGTGCACTACAGGGGAGCAATAGGCAAGTCTCTACCCCCTTCAACGTGAGTATGCGCCAGATTGCACGGTACCGGGCGACTTCCACACCTCTTTCGTGTACGCGAGAATCACGGTATAATCTGAACCCTGCCCTCGCTAGAATGGGAGACCAGCATATTACTCACCCATCGAATCAGCCCGCGACGAGATAG"
expected = "MAQEGTSWFSPAKGSLIVNANPGTSSSHCKGIATVVRTYRCVVSISLEAGSPKVLAPSHCGANIVVQDKTFNIGILPKRTRSCSAGSGLESSCGYIYSLASAIIEEYPRAYILTLIGIQSLYRQTARNQADPIFSSLHKEVSAHHHVRLPNVLAPGGEARLSHSDSSIVGTKARGQRFVLRCETIANFVRLAISSELMQLSICRSYYWAVDEGPDLVGLAIIRRKRRGCVSKVGARRAWLCSLTAGPYSVHPNSQSSDLFGMDLKGCRAVFHMLDNPINLTSTQSTSSPTRDNVGLICRPILLSPLLSGSSLMTRRPAPYLTLCRTIALLSDRLRLLTMMVLPHLRRERHTRQCLRGVQSLTSTYDWTKRKEPHISCNDERADALDKKATLAACQATKGVYDWRLHALPNYPLEDAQDDVGPDATLKLGSPGKKRAAICKHCRGRVVLLVLRVRVDCLWEDRRCTNADIQRTLIISARPKRWRPIANHPRRSECIEFLHVFERRKVDKPSRSRFRANCCRCEISSWCSCSSPETFTECIKQAILACFKGCKGNFACRHARGCVGTWDHSRATLTLLVVYILEEYGAKAANRKSLSFGTSPNISQEAGPEGCCPVGAVDRSNHLGGSLLVFICCFTRDTVQKDRSRGFFSPAMLFRLIKCLVLMIESSSACSFCFPASPFAIRVRVASGDLTDRIAWVLFPINTPRLPGTHLFRTCYEVVNVYTWNPPPAGQFNLSVSGGFFTAGDALCTRHCGCLCMCETPGWILEISGPPVSDESVLNAGQNESRRSTDNHESNYRPGVTGPWQYMMCGRVFHPVNASLSTDVEDHAQRSRIILQVADFSVICPVGAIRSGRVFKIFIERIQGRLDSVCNKTSRGTQQQRAHLVILHSAVRFLPDDIFSFLDSSVTGVRSEVSTHLSCGLNRPFSRNLSGTSRSRLPDGGSCTRMILWFSSSASSRGLRVVTKHHRGLEQSNNSRRHLLLVLEVQLSSYDLPILRYRKVYGHSGWRVLEATLFLDESIWRVNAQTILDSHRPTVSAYALGESKQHPKSLKTASVPLSDRTSPISSPSSSERLLNTHIEIRISPYAVLQDHLCTEGSLDKHREVSRRFGAENLYMHSVVSKRSKMIDVVVSASQNLEGQAVRKPLFFILIKCCLNNPAPRCATLGPSPIHPRLQHKRLIKMAMAPSGCMDHPRGRTIVALHSNAKKFLLSHCSPAILLYKPSLNGQLEVKPDLVILTLVLCLSSQAYIRSTTHHGSTSRHPTYFCPQLNPDCCPRQTGRLEKVVVGKSTSVPRGIRPLTRYTVHFLEMYAQSDGLPISERAEPVIPVPLIMFRVRLRTSLHNRYTQCIRATLLTQAGRGKTRRIHQTPVPNFVLCVAMSVREVISCVGWLSISIAVHQIYGNEKLGLDEVCVHPTAEFPYVGWAVLFVLNRIYTAYPSLKDMHINTYLLRICSTLTVNGLTWVHVQDPLSGKLLLGVNTIFPMRSIVQQRATISSTGKKAPIAPPSRPSKWELFRKRREVYPIGYRLSSHPICRHVRMCSLERSGAAHHQPGLLSMLVVHGSYTSVWRTMMGYVEVPKSNTSLSRTGVPSFSSKRKDIRTKDVKVWIPMSRAGHASRNACYFRKPSQRCRYLTSAFKSPSWAGNHRPNSMCRTIPSFSLTLNPNGSPAGFCGEGLLESKRDLRMRFFKPTTPSGCLVMSLLIYDENMRGCIDWRCRPITRRSFPQGHLLLRSKIIDSDYERANSMSSESKGVRVDRCGLLRSASLGRRSIPRSLQKLCLGALTHRTMKAPTGCKSLKDCSGEGHASGSVSIHDHKFDNGARPSPKGLLTPGVIVSLIRLLLSVHQGSLGLAHSFPGAACCWLQSRLFRSRIMLASCRGSWHEIEWPCLRSDACPRSLAYAGHSANSNILPRTCRYAKPLHIATRVSKKTCAQGYSVRSTAFILRMVLPSGSPRLCKLCILSAIERDWGGIGICTQCGTNYTTGSTKLRSGRRYIEGYFLSCSRSSEVVLLNIIGTNGRCRKPTDRSHGGSASKDCFAETVALDIQLFAPHRPRMFNRSRTTASNSRFKHYAYGTGPHAYFQGHLTASLATSCGPKVTLRHYKGRLYFPPSLGGTQGDLNAISVLFMQSLAGEPPRPWRTPRQQKIERCHLRLDLKGSTHAQKDGYYGWSLILTTAGPSRVALRGRHCTSNGFYGGNALCIYLILFPVLSPDVCNCGIHLSPPTLLNGVLRGYVVDVLSRPACVWCCRDPDPRNHPSQIGPEFGLGFLHGRPFRTHHHTTTACCEGQGPCSEYKTQFTCRLRGALLIVSGRMPSQLCGCFEHPSYIPAPVLQSQWLCAGTACGVRPSLCSCVAHFTGLTPTTKLLPTLCVGVDTDVKRKIMQSLWGYRSKGRLLRLWPTWLTHVPKGNFRNGSLSSISVVATDIAILFVVMSLKLSLFSGMRNFARSETFHDYCVVPFAILGAGGLIQYCWRQSLFPTAMMPRFYEEVAVTFTGWADSRDTVLVKDLSSIPVECRSAYSVTLPGIGKWRAYLGRPLPTCCAFRCSNQTYCGLRVQIDVYLRSGMTETVVRVHMCCRRAILALTECRNGVRQAKCPGIMEFHSDAGAFNLHACSVLLRTLRYGPVELPSLPIVMVEGEPARSPGAVRVCRLKVSYLQISSLLHAGLSHSPMRLNHGSDWFGLCSRIFRHRLFLLTDSISDAKTRLYFRTVQCAKRRLPKCAQGHVCSPTSTTGPRWQTPGKHKLRISLPSSCRQRLCRRRKWAISPDMETLRMAALWSSVLTQLGFCDQFNILTCMGGSRWISPENLDSLRLHQRFSALSTPLTEIISLGETLSSGLLCSIRARRSDDDQSRNPAKILVGAPRTFALGLVTTNTGKVGHGSQTCLSRCDLFPRPGTGDHISDVSANFGAVSGFYRKNEALAKNYTLVIQFNVPAARCDDRICVKEQGLSLTCFPESFQHCHVPRVTPNHCLIRTRVPLLRPSPTPHRGLYQCHRGALQGSNRQVSTPFNVSMRQIARYRATSTPLSCTRESRYNLNPALARMGDQHITHPSNQPATR"

# https://biopython.org/docs/1.75/api/Bio.Data.CodonTable.html
# https://ftp.ncbi.nih.gov/entrez/misc/data/gc.prt
codon_tables = [1,2,3,4,5,6,9,10,11,12,13,14,15,16,21,22,23,24,25,26,27,28,29,30,31,32,33]
for table in codon_tables:
    translated = translate(coding_dna, table, stop_symbol="")
    if expected == translated or expected == translated[0:-1]:
        print(table)