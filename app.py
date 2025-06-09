
import streamlit as st
from openai import OpenAI

st.title("AI 스타일링 텍스트 프롬프트 생성기")

api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

group_name = st.text_input("🎤 그룹명", "미정")
member_count = st.slider("👥 멤버 수", 1, 10, 4)
style_keyword = st.text_input("✨ 스타일 키워드", "자존감 넘치는 퀸들")
gender = st.radio("성별", ["여자", "남자"], index=0)

if st.button("프롬프트 생성하기"):
    if not api_key:
        st.warning("API 키를 입력해주세요.")
    else:
        prompt = f"{member_count}인조 {gender} 아이돌 그룹 '{group_name}'의 스타일링을 제안해줘. 스타일 키워드는 '{style_keyword}'이고, 각 멤버의 개성도 살려줘. 옷차림, 헤어스타일, 소품 등을 포함한 구체적인 설명을 프롬프트 형태로 만들어줘."

        client = OpenAI(api_key=api_key)

        try:
            chat_response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8
            )
            result = chat_response.choices[0].message.content
            st.success("✅ 생성 완료!")
            st.text_area("📝 스타일링 프롬프트", result, height=300)
        except Exception as e:
            st.error(f"❌ 오류 발생: {e}")
