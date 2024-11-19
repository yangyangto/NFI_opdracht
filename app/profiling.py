from app.models import (
    NucleotideBase,
    IupacNucleotideCodeBase,
    DNASpoor,
    DNAProfiel
)


def profiel_past_in_spoor(dna_spoor: DNASpoor, dna_profiel: DNAProfiel) -> bool:
    if len(dna_profiel.sequentie) != len(dna_spoor.sequentie):
        return False
    elif dna_profiel.sequentie == dna_spoor.sequentie:
        return True

    for i in range(len(dna_profiel.sequentie)):
        profiel_base = NucleotideBase(dna_profiel.sequentie[i])
        spoor_base = IupacNucleotideCodeBase[dna_spoor.sequentie[i]]
        if not spoor_base.matched_nucleotide_base(profiel_base):
            return False
    return True
