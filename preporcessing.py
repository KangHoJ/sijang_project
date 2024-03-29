def category(item):
  su_list = ["갈치", "고등어", "멸치", "조개", "게", "새우", "오징어", "낙지", "문어", "해삼", "고래", "바다", "물고기" , '활' , '가자미' , '명태' , '어','홍합','소라','굴',
             "근대", "깐 바지락", "냉태", "대구", "달래", "매생이", "머위대", "삼치",'조기' ,"부세", "주꾸미",'바지락','미역','가오리','가리비'
             ,'꼬막','다시마','꽁치','꼴뚜기','대합']

  ve_list = ["가지", "감자", "양파", "배추", "무", "당근", "토마토", "오이", "버섯", "고추", "피망", "깻잎", "시금치", "열무", 
             "콜리플라워", "브로콜리", "아스파라거스",'중하'
              "양배추", "샐러리", "케일", "깻잎", "깻잎순", "쑥갓" ,'고구마','고수','로메인','호박','미나리','콜라비','미더덕',
              '아귀','칼리',"김", '연근','오디','중하'
              "깐마늘", "냉이", "노랑 파프리카", "당귀잎", "대파", "동죽", "레드 치커리","생표고", "나물" , '파','청초','참두릅',
                 "로케트 루꼴라", "매생이", "머위대", "바실",  "부추", "블루베리", "비타민",'마늘'"비트", "빨강 파프리카", 
                 "상추", "생표고", "셀러리", "아욱","양송이", "부추","오만둥이", "적근대", "적상추", "쪽파", "쫑상추", 
                 "참두릅", "청경채",'콩','잎','도루묵','딜','복분자','비트','비름','유자','석류','수삼','아로니아','씀바귀',
                 "취나물", "치커리",'루꼴라','갓','머위잎','마늘','옥수수','파슬리','죽순','쑥','생강','건토란대','그린빈스', '논우렁', '맛',]
  
  fru_list = ['귤','배','사과','샤인머스캣','파인애플','수박','딸기','멜론','바나나',"단감", "만감",'앵두',
              "참외", "오렌지",'감','복숭아','키위','자두','망고','자몽','포도','체리','레몬','살구','아보카도','대추','모과','매실']
 
   
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


def good_lower_day(df):
  top_index = df.groupby('category_name')['value'].nlargest(5).index.values
  number_list = []
  for category_name, value in top_index:
      number_list.append(int(value))
  category_cheaper_data = df.loc[number_list]
  return category_cheaper_data



# # 성능 평가를 위해 y_test제작 (연습용)
# def y_test_fun(item):
#     fru_list = ["키위"]
#     ve_list = ['머위잎','파슬리']
#     for keyword in ve_list:
#         if keyword in item:
#             return "야채"
#     for keyword in fru_list:
#         if keyword in item:
#             return "과일"
          
          