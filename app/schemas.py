from pydantic import BaseModel


class DNAMatchResponse(BaseModel):
    '''Response Model van een DNA vergelijking'''
    is_match: bool
    DNA_spoor: str
    DNA_profiel: str
