from fastapi import FastAPI
from datetime import datetime
import random
import pytz
from typing import Dict

app = FastAPI(
    title="API de Utilidades",
    description="API simples com endpoints para gerar números aleatórios e obter horário atual",
    version="1.0.0"
)

@app.get("/")
def read_root() -> Dict[str, str]:
    """Endpoint raiz com informações da API"""
    return {
        "message": "Bem-vindo à API de Utilidades!",
        "endpoints": {
            "números aleatórios": "/random",
            "horário atual": "/time"
        }
    }

@app.get("/random")
def generate_random_number() -> Dict[str, int]:
    """Gera um número aleatório entre 0 e 1000"""
    random_number = random.randint(0, 1000)
    return {"random_number": random_number}

@app.get("/time")
def get_current_time() -> Dict[str, str]:
    """Retorna o horário atual em formato ISO"""
    # Obtém o horário atual em UTC
    utc_now = datetime.utcnow()
    # Converte para o fuso horário de São Paulo (pode ser ajustado conforme necessário)
    tz = pytz.timezone('America/Sao_Paulo')
    local_time = utc_now.replace(tzinfo=pytz.utc).astimezone(tz)
    
    return {
        "current_time": local_time.isoformat(),
        "timezone": "America/Sao_Paulo"
    }

# Para ambientes de desenvolvimento/local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)