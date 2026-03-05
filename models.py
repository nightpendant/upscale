from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    proposal_text: str
    action: str
