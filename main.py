import streamlit as st

st.title("나의 첫 웹서비스!!")
name = st.text_input("이름을 입력해주세요.")
menu = st.selectbox('가장 많이 쓰는 앱은?',['인스타그램', '페이스북', '카카오톡', '유튜브'])
time = st.slider('하루 사용시간은?', 0,24,3)

if st.button('결과 보기'):
    # Provide progressive warnings based on daily usage hours
    if time < 2:
        warning_msg = '지금은 괜찮지만, 하루 중 짧은 시간이라도 꾸준히 쉬는 습관을 들여보세요.'
    elif time < 5:
        warning_msg = '사용 시간이 조금씩 늘고 있어요. 1시간마다 눈 건강 체크 시간을 꼭 확보하세요.'
    elif time < 8:
        warning_msg = '하루 절반 가까이 화면을 보고 있네요! 저녁에는 디지털 디톡스 시간을 정해보면 어떨까요?'
    else:
        warning_msg = '하루 대부분을 화면 앞에서 보내고 있어요. 지금 바로 자리에서 일어나 스트레칭과 휴식을 취해보세요.'

    st.write(f'{name}님! {menu}를 하루 평균 {time}시간 사용하시네요.')
    st.warning(warning_msg)
    st.balloons()
