def category(item):
  su_list = ["갈치", "고등어", "멸치", "조개", "게", "새우", "오징어", "낙지", "문어", "해삼", "고래", "바다", "물고기" , '활' , '가자미' , '명태' , '어','홍합','소라','굴',
             "근대", "깐 바지락", "냉태", "대구", "달래", "매생이", "머위대", "삼치",'조기' ,"부세", "주꾸미"]

  ve_list = ["가지", "감자", "양파", "배추", "무", "당근", "토마토", "오이", "버섯", "고추", "피망", "깻잎", "시금치", "열무", "콜리플라워", "브로콜리", "아스파라거스",
              "양배추", "샐러리", "케일", "깻잎", "깻잎순", "쑥갓" ,'고구마','고수','로메인','호박','미나리','콜라비','미더덕','아귀','칼리',"김", 
              "깐마늘", "냉이", "노랑 파프리카", "당귀잎", "대파", "동죽", "레드 치커리","생표고", "나물" , '파'
                 "로케트 루꼴라", "매생이", "머위대", "바실",  "부추", "블루베리", "비타민",
                 "비트", "빨강 파프리카", "상추", "생표고", "셀러리", "아욱","양송이", "부추",
                 "오만둥이", "적근대", "적상추", "쪽파", "쫑상추",  "참두릅", "청경채",
                 "취나물", "치커리",'루꼴라']
  fru_list = ['귤','배','사과','샤인머스캣','파인애플','수박','딸기','멜론','바나나',"단감", "만감", "참외", "오렌지"]

  # 품목명에 키워드 포함 여부 확인
  for keyword in su_list:
    if keyword in item:
      return "수산물"
  for keyword in ve_list:
    if keyword in item:
      return "야채"
  for keyword in fru_list:
    if keyword in item:
      return "과일"
  return "기타"


def get_category_list(df):
    lst = list(df[df['category']=='기타']['PUMNAME'].values)
    return lst



# 성능 평가를 위해 y_test제작 (연습용)
def y_test_fun(item):
    fru_list = ["키위"]
    ve_list = ['머위잎','파슬리']
    for keyword in ve_list:
        if keyword in item:
            return "야채"
    for keyword in fru_list:
        if keyword in item:
            return "과일"