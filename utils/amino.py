from math import floor
import regex
from decimal import Decimal

from .nucleic import dna_to_complement

DNA_CODON = {
    "TTT": "F",
    "TTC": "F",
    "TTA": "L",
    "TTG": "L",
    "TCT": "S",
    "TCC": "S",
    "TCA": "S",
    "TCG": "S",
    "TAT": "Y",
    "TAC": "Y",
    "TAA": "X",
    "TAG": "X",
    "TGT": "C",
    "TGC": "C",
    "TGA": "X",
    "TGG": "W",
    "CTT": "L",
    "CTC": "L",
    "CTA": "L",
    "CTG": "L",
    "CCT": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAT": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGT": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",
    "ATT": "I",
    "ATC": "I",
    "ATA": "I",
    "ATG": "M",
    "ACT": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAT": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGT": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",
    "GTT": "V",
    "GTC": "V",
    "GTA": "V",
    "GTG": "V",
    "GCT": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAT": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGT": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G",
}

AA_MASS = {
    "A": Decimal("71.03711"),
    "C": Decimal("103.00919"),
    "D": Decimal("115.02694"),
    "E": Decimal("129.04259"),
    "F": Decimal("147.06841"),
    "G": Decimal("57.02146"),
    "H": Decimal("137.05891"),
    "I": Decimal("113.08406"),
    "K": Decimal("128.09496"),
    "L": Decimal("113.08406"),
    "M": Decimal("131.04049"),
    "N": Decimal("114.04293"),
    "P": Decimal("97.05276"),
    "Q": Decimal("128.05858"),
    "R": Decimal("156.10111"),
    "S": Decimal("87.03203"),
    "T": Decimal("101.04768"),
    "V": Decimal("99.06841"),
    "W": Decimal("186.07931"),
    "Y": Decimal("163.06333"),
}

START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]


def dna_to_peptide(seq: str) -> str:
    seq = seq[:-3] if seq[-3:] in STOP_CODONS else seq
    return "".join(
        [DNA_CODON[seq[i * 3 : i * 3 + 3]] for i in range(floor(len(seq) / 3))]
    )


RE_ORF = regex.compile(
    rf"{START_CODON}(?:(?!{"|".join(STOP_CODONS)})\w{{3}})*(?:{"|".join(STOP_CODONS)})"
)


def dna_locate_orfs(seq: str) -> list[str]:
    ma = RE_ORF.findall(seq, overlapped=True)
    mb = RE_ORF.findall(dna_to_complement(seq), overlapped=True)
    return list(set(ma + mb))
