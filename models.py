from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    action: str
    project_name: str
    advisor: str
    venue: str
    date: str
    description: str
    type: str
    strands: list[str]
    learning_outcomes: list[str]
