from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola, soy tu IA avanzada. ¿En qué puedo ayudarte?"}
