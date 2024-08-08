from pydantic import BaseModel

from src.schemas.activity_page import ActivityPage
"""
1. Usuário faz req com ID, Linguagem e Nome 
2. Backend solicita ao DB na coleção de ActivityInfo pelo id : LING_ID, Ex: PT_BR0001
3. DB retorna ActivityInfo
4. Backend solicita ao DB na coleção de ActivitySteps com o mesmo id do passo 2, comuma requisição que retorna vários valores os quais o activityInfoId é igual ao do passo 2
5. Backend retorna ao Usuário o ActivityRequest
"""

class ActivityOptions(BaseModel):
    title : str
    response : str

class ActivitySteps(BaseModel):
    pageType: str
    context : str
    question : str
    options : list[ActivityOptions]
    answerOptionIndex : int
    responses : list[str]

class ActivityInfo(BaseModel):
    activityInfoId: str
    activityScore: int
    title : str
    subtitle : str
    question : str
    steps : list[ActivitySteps]

class ActivityRequest(BaseModel):
    activityScore : int
    title : str
    subtitle : str
    question : str
    steps: list[ActivitySteps]
    
class Activity(BaseModel):
    activityInfoId : str
    activityScore : int
    title : str
    subtitle : str
    question : str
    nameOcorrences : list[int]
    steps: list[ActivityPage]