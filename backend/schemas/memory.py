from pydantic import BaseModel

class MemoryUpdate(BaseModel):
    architecture: str
    tech_stack: str
    decisions: str
    conventions: str