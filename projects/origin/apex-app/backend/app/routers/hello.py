"""Hello-world endpoint — Issue 01 scaffolding verification"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/api/hello")
def hello():
    return {"msg": "hello"}
