import pytest
from app.models import DNASpoor, DNAProfiel


def test_dna_spoor(dna_spoor_seq):
    """Test initalisatie DNASpoor en (class)methods"""
    dna_spoor = DNASpoor(dna_spoor_seq)
    assert dna_spoor.sequentie == dna_spoor_seq
    assert dna_spoor._allowed_chars() == "ATCGWSMKRYBDHVN"
    assert not dna_spoor._validate_sequentie()


def test_dna_profiel(dna_profiel_seq_passend):
    """Test initalisatie DNAProfiel en (class)methods"""
    dna_profiel = DNAProfiel(dna_profiel_seq_passend)
    assert dna_profiel.sequentie == dna_profiel_seq_passend
    assert dna_profiel._allowed_chars() == "ATCG"
    assert not dna_profiel._validate_sequentie()


def test_dna_spoor_invalide(dna_spoor_seq_invalide):
    """Test error bij initalisatie DNASpoor bij invalide input"""
    with pytest.raises(ValueError):
        DNASpoor(dna_spoor_seq_invalide)
