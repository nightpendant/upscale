from fastapi import FastAPI, HTTPException
from models import AnalysisRequest
from prompts import PROMPTS
from llm import query_llm

app = FastAPI()

@app.post("/analyze")
async def analyze(request: AnalysisRequest):

    if request.action not in PROMPTS:
        raise HTTPException(status_code=400, detail="Invalid action")

    prompt_template = PROMPTS[request.action]

    prompt = prompt_template.format(
        project_name=request.project_name,
        advisor=request.advisor,
        venue=request.venue,
        date=request.date,
        description=request.description,
        type=request.type,
        strands=request.strands,
        learning_outcomes=request.learning_outcomes,
    )

    result = await query_llm(prompt)

    return {
        "action": request.action,
        "analysis": result
    }
