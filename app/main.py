from fastapi import FastAPI, HTTPException
from app.profiling import profiel_past_in_spoor
from app.models import DNASpoor, DNAProfiel
from app.schemas import DNAMatchResponse
# import time
app = FastAPI()


@app.get("/")
def read_root():
    return {"Let's": "Start DNA Profiling"}


@app.get("/dna_profiling")
def match_dna_sequenties(
    dna_spoor_seq: str,
    dna_profiel_seq: str
) -> DNAMatchResponse:
    try:
        dna_spoor = DNASpoor(dna_spoor_seq.upper().strip())
        dna_profiel = DNAProfiel(dna_profiel_seq.upper().strip())

        return {
            "is_match": profiel_past_in_spoor(dna_spoor, dna_profiel),
            "DNA_spoor": dna_spoor.sequentie,
            "DNA_profiel": dna_profiel.sequentie
        }

    except ValueError as e:
        raise HTTPException(status_code=422, detail=e.args)
