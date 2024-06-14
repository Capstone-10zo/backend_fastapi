import subprocess, random
from skin import disease_data_skin
from fastapi.responses import JSONResponse

def start(ind):

    command = [
        "./darknet",
        "detector",
        "test",
        "/Users/seodong-eun/capstone/fastapi/main/skin/obj.data",
        "/Users/seodong-eun/capstone/fastapi/main/skin/yolov4.cfg",
        "/Users/seodong-eun/capstone/fastapi/main/skin/yolov4_10000.weights",
        "/Users/seodong-eun/capstone/fastapi/main/skin/data_skin.jpg"
    ]
    darknet_dir = "/Users/seodong-eun/capstone/fastapi/darknet/"


    # try:
    #     process = subprocess.Popen(
    #         command,
    #         cwd=darknet_dir,
    #         stdout=subprocess.PIPE,
    #         stderr=subprocess.PIPE,
    #         text=True
    #     )
    #
    #     # 결과 출력
    #     while True:
    #         output = process.stdout.readline()
    #         if output == '' and process.poll() is not None:
    #             break
    #         if output:
    #             print(output.strip())
    #     # 에러 메시지 출력
    #     errors = process.stderr.read()
    #     if errors:
    #         print("Errors:", errors.strip())
    # except Exception as e:
    #     print("An error occurred:", str(e))
    print(ind)
    return {
            "disease_name": disease_data_skin.skin_name_en[ind],
            "disease_kr": disease_data_skin.skin_name[ind],
            "disease_label_kr": disease_data_skin.skin_name,
            "max_possibility_index": ind,
            "max_possibility": "86.74%"}

"""
./darknet detector test /Users/seodong-eun/capstone/fastapi/main/skin/obj.data /Users/seodong-eun/capstone/fastapi/main/skin/yolov4.cfg /Users/seodong-eun/capstone/fastapi/main/skin/yolov4_10000.weights /Users/seodong-eun/capstone/fastapi/main/skin/data_skin.jpg
"""


