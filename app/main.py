from fastapi import FastAPI, HTTPException
from app.profiling import profiel_past_in_spoor
from app.models import DNASpoor, DNAProfiel
from app.schemas import DNAMatchResponse


app = FastAPI()


def preprocess_seq(sequence: str) -> str:
    """
    Preprocessed de sequentie door spaties te strippen en kleine letters te
    vervangen door hoofdletters. 
    Note. zou in een andere file moeten, maar voor nu overbodig.
    """
    return sequence.strip().upper()


@app.get("/")
def read_root():
    return {"Let's": "Start DNA Profiling"}


@app.get("/dna_profiling")
def match_dna_sequenties(
    dna_spoor_seq: str,
    dna_profiel_seq: str
) -> DNAMatchResponse:
    """
    Vergelijkt DNA spoor met een DNA profiel en geeft terug of het een match is.
    Bij invalide input, wordt er een exception geraised.
    """
    
    try:
        dna_spoor = DNASpoor(preprocess_seq(dna_spoor_seq))
        dna_profiel = DNAProfiel(preprocess_seq(dna_profiel_seq))

        return {
            "is_match": profiel_past_in_spoor(dna_spoor, dna_profiel),
            "DNA_spoor": dna_spoor.sequentie,
            "DNA_profiel": dna_profiel.sequentie
        }

    except ValueError as e:
        raise HTTPException(status_code=422, detail=e.args)
