from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import events, rules, executions

models.Event.metadata.create_all(bind=engine)
models.Rule.metadata.create_all(bind=engine)
models.Execution.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Automation Platform")

app.include_router(events.router)
app.include_router(rules.router)
app.include_router(executions.router)

@app.get("/")
def root():
    return {"message": "Mini Automation Platform rodando!"}