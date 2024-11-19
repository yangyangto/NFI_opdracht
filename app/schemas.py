from pydantic import BaseModel


class DNAMatchResponse(BaseModel):
    is_match: bool
    DNA_spoor: str
    DNA_profiel: str
