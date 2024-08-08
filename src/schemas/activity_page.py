from pydantic import BaseModel

class Options(BaseModel):
    title: str
    response : str

class MultipleChoices(BaseModel):
    context : str
    question : str
    options : list[Options]
    correctIndex : int
    pontuation : int

class ResponseIntro(BaseModel):
    texts : list[str]

class ResumeBlock(BaseModel):
    texts : list[str]
    resumeBlocks : list[int]

class ActivityPage(BaseModel):
    pageType:str
    content : MultipleChoices|ResponseIntro|ResumeBlock
