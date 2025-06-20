from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    # TODO: Save to MongoDB, produce to Kafka
    return {"filename": file.filename}

@router.post("/query")
async def query_chatbot(prompt: str):
    # TODO: Query OpenAI and search MongoDB
    return {"response": "placeholder"}
