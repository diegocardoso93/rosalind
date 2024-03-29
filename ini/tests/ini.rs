use ini::*;

#[test]
fn ini_test1() {
    let seq = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC";

    assert_eq!(ini(seq), "20 12 17 21");
}

#[test]
fn ini_test2() {
    let seq = "GGCTTTAGCTACACATACTGGCAGACGAAACTGAGCAGGTAATCATTCTAGTCACGTCTAGTTGATTTCACACCCTCGATGAAAACGACCGCAGCTCGGAGAGACGATAGTGGTGGTTTCTGACCATACCCTTAGTTTTACCGGCATACCTCAAAACAGCTTGATGCAGAGGCGGCTCTGCCATATGGTTCAGATTCGCTCCGGGGCCGTTTCCTAGGAATCTCTTCAGGTTGGTCCCAGAAAAAGATTCGTCGGGTGCAGCGCAACCCACGGTTTCGCTGAAACATCCTTTCGACTCCCCACTCTAGCGGCCGACCCCGCCTAACCGCCCTGATGCCCTACACTATATTAGAAATTTTGTAGAGGCAAGCCTGCGATCTACTGATATGGCCCAAGGAACACACTTGAATTGGCAACAAGCTGCTTAGGTTGGCCAAAAATACTCATTCTGTGGCACTTCATCCATCCTGCGTGCAACCGAGAAGCTAAAAAATCCACCGGCAAATAGAGGAAGACACCGTCTCTGAAGTTAGAATCGCACGCGCGCGAGGTCCCTACGCGGCACCATAGCTGGCTAAAACCCTGTACGAGGCGACGCTCTATTAGGGACTTGTCTCGAAATACACAGGGATACTCGCGTAGAATAATTCAGGGGTCACCTCGTGATGCCTTTGCGCACCGGAATTATGGGATTGAATAATAGCCGGTGACGACTTTCTCTTAAACTGAGGAGCCATCTTGGTATGAGGCTTGGTTCCAGACCTAAGATATCGATCTCAGCCTAAACAAGAAACCCCTGTCCCCTGTTATTACCTATCTAAGAGTCTGTAGAAGTTTGAAAATACGCTGCGGGGCGGACCTTAATGTACTATTTTAGCGTGACCGTGACCTGC";

    assert_eq!(ini(seq), "233 235 210 215");
}
