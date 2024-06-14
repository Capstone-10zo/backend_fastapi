from disease_data import *
from tensorflow.keras.models import load_model
import numpy as np


def run_models(image):
    processed_image = preprocess_image(image)
    model = load_model("model/disease_model2.h5")
    result = model.predict(np.array([processed_image])).tolist()[0]
    max_ind = result.index(max(result))

    disease_name_kr = disease_k[max_ind]

    print(result)

    return {"disease_name": disease_label[disease_name_kr],
            "disease_kr": disease_name_kr,
            "disease_label_kr": disease_k,
            "result": result,
            "max_possibility_index": max_ind,
            "max_possibility": "%.2f%%" % (result[max_ind] * 100)}


def preprocess_image(image):
    # 이미지 크기 조정 및 스케일링
    image = image.resize((224, 224))  # 모델에 맞는 크기로 조정
    image = np.array(image)
    image = image / 255.0  # 이미지 픽셀 값을 [0, 1] 범위로 스케일링
    return image


