from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticador():
    return {"Mensagem": "Você acessou a página de autenticação", "autenticado": False}
