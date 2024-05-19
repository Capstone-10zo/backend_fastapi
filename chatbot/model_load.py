from .qna_bot import load_qna_bot

def load_qna(request):
    # 저장된 파일 로드 -> QnABot 클래스 인스턴스 생성
    loaded_qna_bot = load_qna_bot('chatbot_model.pkl')

    # 사용자 입력에 대한 답변 예측
    user_input = request
    similar_question, predicted_answer, similarity_score = loaded_qna_bot.predict_answer(user_input)
    return {"입력 질문":user_input, "유사한 질문": similar_question,
            "예측 답변": predicted_answer, "유사도": similarity_score}

    # 결과 출력
    # print('입력 질문:', user_input)
    # print('유사한 질문:', similar_question)
    # print('예측 답변:', predicted_answer)
    # print('유사도:', similarity_score)

