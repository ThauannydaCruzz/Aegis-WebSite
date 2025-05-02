from fastapi import FastAPI
from database import Base, engine
from routes import auth

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Registrar rotas
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])