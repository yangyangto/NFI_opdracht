import pytest


@pytest.fixture
def dna_spoor_seq():
    return "ATTCGWTTBATTVGCT"


@pytest.fixture
def dna_profiel_seq_passend():
    return "ATTCGATTGATTAGCT"


@pytest.fixture
def dna_profiel_seq_niet_passend():
    return "ATTCGATTAATTAGCT"


@pytest.fixture
def dna_spoor_seq_invalide():
    return "ATTCGWTTBATTVGCZ"
