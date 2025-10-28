from fastapi import APIRouter
import requests


router = APIRouter(prefix="/cep", tags=["CEP"])


@router.get("/{cep}")
async def pegar_cep(cep: str):
    url = f"https://viacep.com.br/ws/{cep}/json"

    r = requests.get(url)
    response = r.json()

    return {"Logradouro": response}