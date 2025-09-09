from pydantic import BaseModel, Field
from typing import Optional

class QueryRequest(BaseModel):
    query: str = Field(..., description="The query to be answered")
    context: Optional[str] = Field(None, description="The context to be used for answering the query")

class QueryResponse(BaseModel):
    answer: str = Field(..., description="The answer to the query")
    source: Optional[str] = Field(None, description="The source of the answer")

    class Config:
        from_attributes = True
