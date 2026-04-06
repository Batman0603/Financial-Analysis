from fastapi import FastAPI
from app.api.routes import auth, upload
from app.core.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance AI App")

app.include_router(auth.router)
app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "Finance AI Backend Running 🚀"}