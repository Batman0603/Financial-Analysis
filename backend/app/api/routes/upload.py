from fastapi import APIRouter, UploadFile, File, HTTPException
import os

router = APIRouter(prefix="/upload", tags=["Upload"])

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith((".xlsx", ".xls")):
            raise HTTPException(status_code=400, detail="Only Excel files allowed")

        file_path = os.path.join(UPLOAD_DIR, file.filename)

        with open(file_path, "wb") as f:
            content = await file.read()
            f.write(content)

        return {"message": "File uploaded successfully", "path": file_path}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))