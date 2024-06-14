from .qna_bot import load_qna_bot

def load_qna(request):
    # 저장된 파일 로드 -> QnABot 클래스 인스턴스 생성
    loaded_qna_bot1 = load_qna_bot('chatbot_model.pkl1')
    loaded_qna_bot2 = load_qna_bot('chatbot_model.pkl2')
    loaded_qna_bot3 = load_qna_bot('chatbot_model.pkl3')

    if "안녕" in request or "물어봐도" in request or "고마워" in request:
        qna_bots = [loaded_qna_bot2, loaded_qna_bot3]
    else:
        qna_bots = [loaded_qna_bot1]
    # 사용자 입력에 대한 답변 예측
    user_input = request
    result = []
    for bot in qna_bots:
        similar_question, predicted_answer, similarity_score = bot.predict_answer(user_input)
        result.append((similarity_score, similar_question, predicted_answer))

        if similarity_score >= 0.8:
            break

    result.sort(key = lambda x:x[0], reverse = True)

    similarity_score, similar_question, predicted_answer = result[0]
    print(similarity_score)
    print(similar_question)
    print(predicted_answer)
    return {"입력 질문":user_input, "유사한 질문": similar_question,
            "예측 답변": predicted_answer, "유사도": similarity_score}

    # 결과 출력
    # print('입력 질문:', user_input)
    # print('유사한 질문:', similar_question)
    # print('예측 답변:', predicted_answer)
    # print('유사도:', similarity_score)

