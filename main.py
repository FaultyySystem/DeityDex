from fastapi import FastAPI
import json

app = FastAPI()

# Carrega a lista de deuses a partir do arquivo de dados JSON
with open("gods.json") as f:
    gods = json.load(f)

# Rota para retornar a lista de deuses
@app.get('/gods')
def get_gods():
    return gods

# Rota para retornar um deus específico
@app.get('/gods/{name_god}')
def get_god(name_god: str):
    for god in gods:
        if god['nome'].lower() == god_name.lower():
            return god
    return {"message": "Deus não encontrado"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=3001)

