from fastapi import APIRouter, HTTPException
from src.firebase.firebase import firebase
from src.schemas.activity import Activity

router = APIRouter()

@router.get("/activity/{actv_id}/", status_code=200, response_model = Activity)
async def get_activity(childs_name: str, actv_id):
    resp = firebase.get_activity(actv_id, name=childs_name)
    if resp is None:
        raise HTTPException(status_code=404, detail='Não existe essa atividade')
    return resp