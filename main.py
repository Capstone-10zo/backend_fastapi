from fastapi import FastAPI, File, UploadFile, HTTPException, Request
from tensorflow.keras.models import load_model
from utils import run_models, preprocess_image
from chatbot import model_load, qna_bot, model_save
from PIL import Image
import numpy as np
import os, io, asyncio
import pandas as pd
import utils2, random

app = FastAPI()

@app.get("/data")
async def data():
    return {"message": "data from fastapi"}


@app.get("/predict")
async def make_prediction():
    script_dir = os.path.dirname(__file__)  # 스크립트 파일 위치
    image_path = os.path.join(script_dir, "data", "d1.png")  # 'data' 폴더 내의 'd1.png'

    # 이미지 파일 존재 확인
    if not os.path.exists(image_path):
        raise HTTPException(status_code=404, detail="Image not found")

    try:
        # 이미지 로드 및 전처리
        with Image.open(image_path) as img:
            processed_image = preprocess_image(img)

            # 모델 예측 수행
            prediction = model1.predict(np.array([processed_image]))

            return {"prediction": prediction.tolist()[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/predict2")
async def make_prediction2(file: UploadFile = File(...)):
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        try:
            return run_models(image)
        except:
            raise HTTPException(status_code=404)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/skin_diag")
async def make_diagnosis_skin(file: UploadFile = File(...)):
    try:
        content = await file.read()
        image = Image.open(io.BytesIO(content))
        await asyncio.sleep(3)
        return utils2.start(1)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chatbot")
async def getResponse(request: Request):
    body = await request.body()
    text = body.decode()
    try:
        return model_load.load_qna(text)

    except HTTPException as e:
        raise HTTPException(status_code = 500)

