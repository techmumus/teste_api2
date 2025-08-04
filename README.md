# Techmumus Teste API2

API simples desenvolvida com FastAPI contendo endpoints para geração de números aleatórios, nomes e obtenção de horário atual.

## Endpoints

- `GET /` - Página inicial com informações da API
- `GET /random` - Gera um número aleatório entre 0 e 1000
- `GET /time` - Retorna o horário atual
- `GET /name` - Gera um nome aleatório

## Deployment no Railway

Esta API está configurada para deployment no Railway. Para fazer o deploy:

1. Crie uma conta no [Railway](https://railway.app/)
2. Conecte seu repositório GitHub
3. Selecione este projeto
4. Railway irá automaticamente detectar e fazer o deploy usando as configurações em `railway.json`

## Desenvolvimento Local

Para rodar localmente:

1. Instale as dependências: