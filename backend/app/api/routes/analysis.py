from fastapi import APIRouter, UploadFile, File
from app.services.analysis_service import process_financial_file

router = APIRouter()


@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = process_financial_file(file)
    return result