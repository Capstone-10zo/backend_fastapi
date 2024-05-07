from disease_data import *
import numpy as np


def run_models(image):
    processed_image = preprocess_image(image)
    for disease in models:
        model = models[disease]
        result = model.predict(np.array([processed_image])).tolist()[0]
        # results.append((max(result), disease))
        ind = result.index(max(result))
        if max(result) >= 0.800:
            return {"disease_name": disease,
                    "disease_kr": disease_kr[disease],
                    "disease_label_kr": disease_label[disease],
                    "result": result,
                    "max_possibility_index": ind,
                    "max_possibility": max(result),
                    "result_label": disease_label[disease][ind]}


def preprocess_image(image):
    # 이미지 크기 조정 및 스케일링
    image = image.resize((224, 224))  # 모델에 맞는 크기로 조정
    image = np.array(image)
    image = image / 255.0  # 이미지 픽셀 값을 [0, 1] 범위로 스케일링
    return image


