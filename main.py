import streamlit as st
import random

# Define the text groups
group_S = ["S등급 [큐트] 울려라, 페스티벌! 여름 밤의 추억 쟈몽]",
            "S등급 [퓨어] 졸업: 우리들의 마지막 장 팍기",
            "S등급 [쿨] 소중하게 움켜쥔 그 기억은 을루",
            "S등급 [퓨어] 원하던 소리를 전달하기 위해서 두만"]
group_A = ["A등급 [쿨] 10 루피를 전달해 준 고론족",
           "A등급 [큐트] 익은 바나나를 먹는 이가단",
           "A등급 [쿨] 수강신청 정도야! 파키",
           "A등급 [퓨어] 잠옷 바지 괴물 을루",
           "A등급 [쿨] 딧슈 파세요의 쟈몽",
           "A등급 [큐트] 콜라보 카페는 내가 접수 두만"]
group_B = ["고블린", "레드 고블린", "블루 고블린", "오렌지 고블린", "퍼플 고블린", "그린 고블린",
           "지나가던 링크", "코로그", "코로그의 똥", "코로그 3단 똥", "누가 잃어버린 것 같은 마라카스"
           "사기꾼 모가단", "타쿠미 씨", "아키의 기타", "ECHOLL 테이프", "꾸의 사원증 (이거 있어야 구내 식당에서 공짜로 밥 먹음)",
           "텐마 츠카사 아크릴 스텐드", "이의있음! 말풍선", "꾸의 스위치", "꾸의 마이크", "꾸의 잠옷 바지", "모쟈가 구매한 똥"]



# Define the probabilities for each group
prob_S = 0.01
prob_A = 0.05
prob_B = 0.94

def get_random_text(group_S, group_A, group_B, prob_S, prob_A, prob_B):
    # Choose a group based on the defined probabilities
    chosen_group = random.choices(
        population=['S', 'A', 'B'],
        weights=[prob_S, prob_A, prob_B],
        k=1
    )[0]

    # Select a random text from the chosen group
    if chosen_group == 'S':
        return random.choice(group_S)
    elif chosen_group == 'A':
        return random.choice(group_A)
    else:
        return random.choice(group_B)
    
result = get_random_text(group_S, group_A, group_B, prob_S, prob_A, prob_B)

def main():
  st.title("두근두근 파키 뽑기")
  st.header("안녕! 파키 뽑기를 해 보세요.")

  st.text(" \n")
  st.text(" \n")
  st.write ("S등급, A등급, 그리고 일반, 총 3등급이 있습니다!")
  st.write ("S등급의 레어 캐릭터를 뽑아 보세요!🐇")
 
  st.text(" \n")
  st.text(" \n")


  button = st.button("팍기뽑기")

  if button:
    response = result
    st.subheader("머가 나왓을가요?:")
    st.write(response)

if __name__ == "__main__":
  main()