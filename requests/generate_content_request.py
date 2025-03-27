from pydantic import BaseModel

class Text(BaseModel):
    text: str

class Parts(BaseModel):
    parts: list[Text]

class GenerateContentRequest(BaseModel):
    contents: list

