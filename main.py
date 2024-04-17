from fastapi import FastAPI, HTTPException
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os

app = FastAPI()
model = load_model("model/model-cataract.h5")  # 모델 파일 경로

@app.get("/data")
async def data():
    return {"message":"data from fastapi"}

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
            prediction = model.predict(np.array([processed_image]))
            return {"prediction": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def preprocess_image(image):
    # 이미지 크기 조정 및 스케일링
    image = image.resize((224, 224))  # 모델에 맞는 크기로 조정
    image = np.array(image)
    image = image / 255.0  # 이미지 픽셀 값을 [0, 1] 범위로 스케일링
    return image