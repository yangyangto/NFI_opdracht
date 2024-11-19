from app.profiling import profiel_past_in_spoor
from app.models import DNAProfiel, DNASpoor


def test_profiel_matches_spoor(
    dna_spoor_seq,
    dna_profiel_seq_passend
):
    dna_spoor = DNASpoor(dna_spoor_seq)
    dna_profiel = DNAProfiel(dna_profiel_seq_passend)
    assert profiel_past_in_spoor(dna_spoor, dna_profiel)


def test_profiel_not_matches_spoor(
    dna_spoor_seq,
    dna_profiel_seq_niet_passend
):
    dna_spoor = DNASpoor(dna_spoor_seq)
    dna_profiel = DNAProfiel(dna_profiel_seq_niet_passend)
    assert not profiel_past_in_spoor(dna_spoor, dna_profiel)
