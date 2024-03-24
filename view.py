from dataload import main_load , Data_load2
from preporcessing import good_lower_day
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

api_df , etc_lst = main_load()
basic_df , country_df = Data_load2()

df = good_lower_day(country_df)
fruit = df[df['category_name']=='과일류']
su = df[df['category_name']=='수산물']
sik = df[df['category_name']=='식량작물']
food = df[df['category_name']=='식품']
vegetable = df[df['category_name']=='채소류']
livestock  = df[df['category_name']=='축산물']
special = df[df['category_name']=='특용작물']

def plot_good_lower_day():
    fig, axs = plt.subplots(3, 2, figsize=(40, 10))
    
    sns.barplot(x="item_name", y="dpr1", data=fruit, ax=axs[0, 0], color="skyblue")
    sns.barplot(x="item_name", y="dpr2", data=fruit, ax=axs[0, 0], color="tomato")
    axs[0, 0].set_title("<어제보다 저렴해진 과일>")
    axs[0, 0].set_xlabel("과일 이름")
    axs[0, 0].set_ylabel("가격")


    # sns.barplot(x="item_name", y="value" ,data=fruit, ax=axs[0,0], color="skyblue")
    # axs[0,0].set_title("<어제보다 저렴해진 과일>")
    # axs[0,0].set_xlabel("과일 이름")
    # axs[0,0].set_ylabel("떨어진 퍼센트")


    sns.barplot(x="item_name", y="value" ,data=su, ax=axs[0,1], color="skyblue")
    axs[0,1].set_title("어제보다 저렴해진 수산물")
    axs[0,1].set_xlabel("수산물 이름")
    axs[0,1].set_ylabel("떨어진 퍼센트")



    sns.barplot(x="item_name", y="value" ,data=sik, ax=axs[1,0], color="skyblue")
    axs[1,0].set_title("<어제보다 저렴해진 식량작물>")
    axs[1,0].set_xlabel("식량작물 이름")
    axs[1,0].set_ylabel("떨어진 퍼센트")


    sns.barplot(x="item_name", y="value" ,data=food, ax=axs[1,1], color="skyblue")
    axs[1,1].set_title("<어제보다 저렴해진 식품>")
    axs[1,1].set_xlabel("식품 이름")
    axs[1,1].set_ylabel("떨어진 퍼센트")
    
    sns.barplot(x="item_name", y="value" ,data=vegetable, ax=axs[2,0], color="skyblue")
    axs[0,0].set_title("<어제보다 저렴해진 채소>")
    axs[0,0].set_xlabel("채소 이름")
    axs[0,0].set_ylabel("떨어진 퍼센트")
    
    sns.barplot(x="item_name", y="value" ,data=livestock, ax=axs[2,1], color="skyblue")
    axs[0,1].set_title("<어제보다 저렴해진 축산물>")
    axs[0,1].set_xlabel("축산물 이름")
    axs[0,1].set_ylabel("떨어진 퍼센트")

    # plt.subplots_adjust(left=0.05, right=0.95 , hspace=0.475 , wspace=0.13)
    plt.show()    
    plt.close()
    
if __name__ == "__main__":
    plot_good_lower_day()