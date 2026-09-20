from pydantic import BaseModel

class DecisionCreate(BaseModel):
    decision: str