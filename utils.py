from disease_data import *
import numpy as np


def run_models(image):
    processed_image = preprocess_image(image)
    results = []
    
    for disease in models:
        model = models[disease]
        result = model.predict(np.array([processed_image])).tolist()[0]
        ind = result.index(max(result))

        results.append((max(result), disease, ind, result))

    results.sort(key=lambda x: x[0], reverse=True)
    final_model = results[0]
    disease_name = final_model[1]

    return {"disease_name": disease_name,
            "disease_kr": disease_kr[disease_name],
            "disease_label_kr": disease_label[disease_name],
            "result": final_model[-1],
            "max_possibility_index": final_model[2],
            "max_possibility": final_model[0],
            "result_label": disease_label[disease_name][final_model[2]]}


def preprocess_image(image):
    # 이미지 크기 조정 및 스케일링
    image = image.resize((224, 224))  # 모델에 맞는 크기로 조정
    image = np.array(image)
    image = image / 255.0  # 이미지 픽셀 값을 [0, 1] 범위로 스케일링
    return image


