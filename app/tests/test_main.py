from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Let's": "Start DNA Profiling"}


def test_match_dna_sequenties(dna_spoor_seq, dna_profiel_seq_passend):
    response = client.get(
        "/dna_profiling",
        params={
            "dna_spoor_seq": dna_spoor_seq,
            "dna_profiel_seq": dna_profiel_seq_passend
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "is_match": True,
        "DNA_spoor": dna_spoor_seq,
        "DNA_profiel": dna_profiel_seq_passend
    }


def test_no_match_dna_profiles(dna_spoor_seq, dna_profiel_seq_niet_passend):
    response = client.get(
        "/dna_profiling",
        params={
            "dna_spoor_seq": dna_spoor_seq,
            "dna_profiel_seq": dna_profiel_seq_niet_passend
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "is_match": False,
        "DNA_spoor": dna_spoor_seq,
        "DNA_profiel": dna_profiel_seq_niet_passend
    }


def test_invalid_input(dna_spoor_seq_invalide, dna_profiel_seq_passend):
    response = client.get(
        "/dna_profiling",
        params={
            "dna_spoor_seq": dna_spoor_seq_invalide,
            "dna_profiel_seq": dna_profiel_seq_passend
        }
    )

    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            "Een DNASpoor mag alleen bestaan uit:ATCGWSMKRYBDHVN\n" +
            "Opgeven sequentie: " +
            dna_spoor_seq_invalide
        ]
    }
