from dataload import main_load
from preporcessing import y_test_fun
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd

def model_process():
    df , etc_lst = main_load()
    # print('분류안된 리스트 ',etc_lst)
    # print('-----------------------'*5)
    X = df.drop('category',axis=1)
    Y = df['category']


    x_train = X[~X['PUMNAME'].isin(etc_lst)]
    y_train =  Y[~(Y.values=='기타')]
    x_test = X[X['PUMNAME'].isin(etc_lst)]
    # print('인코딩 하기전 : ' ,x_train.shape, y_train.shape , x_test.shape)
    # print('-----------------------'*5)



    combined_data = pd.concat([x_train, x_test], axis=0) 
    '''
    아래에 붙이는 이유는 필요한 데이터만 추출해서 분리시킨후 아래로 배치 시키려고
    따로 train,test로 각각 라벨 인코딩을 적용하면 train에 없는 데이터가 test에 있다고 인코딩이 진행되지 않는다.
    (테스트 데이터에 학습 데이터에 없는 카테고리가 포함오류)
    '''
    cat_col = combined_data.select_dtypes(include='object').columns
    le = LabelEncoder()
    for column in cat_col:
        combined_data[column] = le.fit_transform(combined_data[column])
    x_train_encoded = combined_data[:len(x_train)]
    test_encoded = combined_data[len(x_train):]



    test_final = x_test.copy()
    test_final['category'] = x_test['PUMNAME'].apply(y_test_fun)
    y_test = test_final['category']

    # print('모델 들어가기전 최종 ' ,x_train_encoded.shape , y_train.shape , test_encoded.shape , y_test.shape)
    # print('-----------------------'*5)

    train_final = pd.concat([x_train, y_train], axis=1) 
    # print('트f',train_final)

    models = [RandomForestClassifier(random_state=2024)]
    for model in models:
        model.fit(x_train_encoded, y_train)
        te_prob = model.predict_proba(test_encoded) #확률
        # print('확률',te_prob)
        tr_pred = model.predict(x_train_encoded) 
        te_pred = model.predict(test_encoded) 
        # accuracy_tr = accuracy_score(y_train, tr_pred) # 학습한건 잘 맞춘다 
        # accuracy_te = accuracy_score(y_test, te_pred)
        
        # print(f"< {model}의 train 정확도 > : ", accuracy_tr)
        # print(f"< {model}의 test 정확도 > : ", accuracy_te)
        train_final['분류'] = tr_pred
        test_final['분류'] = te_pred
        # print(train_final)
        # print(test_final)
        # print(x_train)
        # print('-----------------------'*10)

    final = pd.concat([train_final, test_final], axis=0) 
    print('최빈값 적용전 final',final)
    # most_common_category = final.groupby('PUMNAME')['category'].agg(lambda x: x.mode().iloc[0]) # 가장 많이 나오는거
    # print(most_common_category[most_common_category.index=='머위잎'])
    # final['분류'] = final['PUMNAME'].map(most_common_category)
    # print(final.tail(10))

    return final

df = model_process()
# print(df)
# if __name__ == "__main__":
#     model_process() # db로 넣기
    
