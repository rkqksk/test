import os
import streamlit as st
import pandas as pd
import datetime
import requests
import base64

url = "https://api.github.com/repos/rkqksk/test/conent/a7210494378232be6cb0e4bce4637278b652d986/data.csv"
token = "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"

data = "col1,col2,col3\nval1,val2,val3"

headers = {
    "Authorization": f"token {token}",
    "Content-Type": "application/json"
}

content = base64.b64encode(data.encode("utf-8")).decode("utf-8")

payload = {
    "message": "Add data to CSV file",
    "content": content
}

response = requests.put(url, json=payload, headers=headers)

if response.status_code == 201:
    print("File created successfully")
else:
    print(f"Error: {response.text}")


# 데이터를 저장할 파일의 경로를 지정합니다.
url = 'https://github.com/rkqksk/test/blob/a7210494378232be6cb0e4bce4637278b652d986/data.csv'

def save_data(data):
    # 입력된 데이터를 CSV 파일에 저장합니다.
    if not os.path.exists(url):
        data.to_csv(url, index=False)
    else:
        existing_data = pd.read_csv(url)
        data = pd.concat([existing_data, data], ignore_index=True)
        data.to_csv(url, index=False)

def main():
    st.title(':blue_book: 작업일반')
    
    # 작업일반_첫 번째 줄
    data = pd.DataFrame(columns=['Date','Time' 'Unit', 'Mold','Product_code','MB'])
    
    # 작업일반_첫 번째 줄
    col1, col2, col3, col4, col5, col6 = st.columns(6) 
    input1 = col1.date_input('Date')
    datetime.date(1900,1,1)
    input2 = col2.time_input('Time',datetime.time(8,00),step=1800)
    input3 = col3.selectbox('Unit',('1호기', '2호기', '3호기', '5호기', '6호기'))
    input4 = col4.text_input('Mold')
    input5 = col5.text_input('Product_code') 
    input6 = col6.text_input('MB')

    # 작업일반_두 번째 줄
    data = pd.DataFrame(columns=['박스사이즈','개입:박스','파레트','발주번호','작업자'])
    
    # 작업일반_두 번째 줄
    col7, col8, col9, col10, col11, col12 = st.columns(6)
    input7 = col7.selectbox('박스사이즈',('중', '대'))
    input8 = col8.text_input('개입:박스')
    input9 = col9.selectbox('파레트',('아주','검정','N/A'))
    input10 = col10.text_input('발주번호')
    input11 = col11.text_input('작업자')


    # 작업일반_세 번째 줄
    data = pd.DataFrame(columns=['고객사','제품명'])
    
    # 작업일반_세 번째 줄
    col12, col13 = st.columns(2)
    input12 = col12.text_input('고객사')
    input13 = col13.text_input('제품명')
    

    st.title(':gear: 조건')
    
    # 조건_첫 번째 줄
    data = pd.DataFrame(columns=['사출시간', '냉각시간', '사출시작시간', '블로우시간', '블로우감압'])
    
    # 조건_첫 번째 줄
    col14, col15, col16, col17, col18= st.columns(5)    
    input14 = col14.text_input('사출시간')
    input15 = col15.text_input('냉각시간')
    input16 = col16.text_input('사출시작시간')
    input17 = col17.text_input('블로우시간')
    input18 = col18.text_input('블로우감압')

    # 조건_두 번째 줄
    data = pd.DataFrame(columns=['기본블로우_1차','보조블로우_2차','스트레치_하강_시작','스트레치_상승_시작'])
    
    # 조건_두 번째 줄
    col19, col20, col21, col22= st.columns(4)
    input19 = col19.text_input('기본블로우_1차')
    input20 = col20.text_input('보조블로우_2차')
    input21 = col21.text_input('스트레치_하강_시작')
    input22 = col22.text_input('스트레치_상승_시작')

    # 조건_세 번째 줄
    data = pd.DataFrame(columns=['장전시간','배압','사출시간'])
    
    # 조건_세 번째 줄
    col23, col24, col25= st.columns(3)
    input23 = col23.text_input('장전시간')
    input24 = col24.text_input('배압')
    input25 = col25.text_input('사출_시간')

    st.subheader('👻 바렐')
    # 조건_네 번째 줄
    
    data = pd.DataFrame(columns=['N','F',"M","R"])
    
    # 조건_네 번째 줄
    col26, col27, col28, col29= st.columns(4)
    input26 = col26.text_input('N')
    input27 = col27.text_input('F')
    input28 = col28.text_input('M')
    input29 = col29.text_input('R')

    st.subheader('👍 핫트런너')
    # 조건_다섯 번째 줄
    data = pd.DataFrame(columns=['블록_S','블록_1','블록_2','블록_3','블록_4'])
    
    # 조건_다섯 번째 줄
    col30, col31, col32, col33, col34= st.columns(5)
    input30 = col30.text_input('블록_S')
    input31 = col31.text_input('블록_1')
    input32 = col32.text_input('블록_2')
    input33 = col33.text_input('블록_3')
    input34 = col34.text_input('블록_4')

    st.subheader('🎧 핫트런너')
    # 조건_여섯 번째 줄
    data = pd.DataFrame(columns=['노즐_1','노즐_2','노즐_3','노즐_4','노즐_5','노즐_6','노즐_7','노즐_8','노즐_9','노즐_10'])
    
    # 조건_여섯 번째 너
    col35, col36, col37, col38, col39, col40, col41, col42, col43, col44= st.columns(10)
    input35 = col35.text_input('노즐_1')
    input36 = col36.text_input('노즐_2')
    input37 = col37.text_input('노즐_3')
    input38 = col38.text_input('노즐_4')
    input39 = col39.text_input('노즐_5')
    input40 = col40.text_input('노즐_6')
    input41 = col41.text_input('노즐_7')
    input42 = col42.text_input('노즐_8')
    input43 = col43.text_input('노즐_9')
    input44 = col44.text_input('노즐_10')

    st.subheader('💫 사출제어')
    # 조건_일곱 번째 줄
    data = pd.DataFrame(columns=['타이머_M2','타이머_M1','위치_p-v','위치_3-2','위치_2-1','위치_샷크기'])
    
    # 조건_일곱 번째 줄
    col45, col46, col47, col48, col49, col50= st.columns(6)
    input45 = col45.text_input('타이머_M2')
    input46 = col46.text_input('타이머_M1')
    input47 = col47.text_input('위치_p-v')
    input48 = col48.text_input('위치_3-2')
    input49 = col49.text_input('위지_2-1')
    input50 = col50.text_input('위치_샷크기')

    st.subheader('💨 사출제어압력')
    # 조건_여덟 번째 줄
    data = pd.DataFrame(columns=['MPA_5','MPA_4','MPA_3','MPA_2','MPA_1'])
    
    # 조건_여덟 번째 줄
    col51, col52, col53, col54, col55= st.columns(5)
    input51 = col51.text_input('MPA_5')
    input52 = col52.text_input('MPA_4')
    input53 = col53.text_input('MPA_3')
    input54 = col54.text_input('MPA_2')
    input55 = col55.text_input('MPA_1')

    st.subheader('🥶 사출제어압력_속도')
    # 조건_아홉 번째 줄
    data = pd.DataFrame(columns=['속도_%_5','속도_%_4','속도_%_3','속도_%_2','속도_%_1'])
    
    # 조건_아홉 번째 줄
    col56, col57, col58, col59, col60= st.columns(5)
    input56 = col56.text_input('속도_%_5')
    input57 = col57.text_input('속도_%_4')
    input58 = col58.text_input('속도_%_3')
    input59 = col59.text_input('속도_%_2')
    input60 = col60.text_input('속도_%_1')

    st.subheader('🍏 충전제어')
    # 조건_열 번째 줄
    data = pd.DataFrame(columns=['PNI','샷크기','MPA_다시흡입위치','압력_MPA_2','압력_MPA_1'])
    
    # 조건_열 번째 줄
    col61, col62, col63, col64, col65= st.columns(5)
    input61 = col61.text_input('PNI')
    input62 = col62.text_input('샷크기')
    input63 = col63.text_input('MPA_다시흡입위치')
    input64 = col64.text_input('압력_MPA_2')
    input65 = col65.text_input('압력_MPA_1')

    # 조건_열한 번째 줄
    data = pd.DataFrame(columns=['속도%2','속도%1'])
    
    # 조건_열한 번째 줄
    col66, col67= st.columns(2)
    input66 = col66.text_input('속도%2')
    input67 = col67.text_input('속도%1')
    
    # "저장" 버튼을 클릭하면 입력한 데이터를 저장합니다.


    if st.button('Save'):
        new_row = {'Date': input1, 'Time': input2, 'Mold': input3, 'Product_code': input4, 'MB':input5,
                   '박스사이즈' : input6, '개입:박스' : input7, '파레트' : input8,'발주번호' : input9,'작업자' : input10,
                   '고객사' : input11, '제품명' : input12, '사출시간' : input13, '냉각시간' : input14, '사출시작시간' : input15, '블로우시간' : input16,
                   '블로우감압' : input17, '기본블로우_1차' : input18, '보조블로우_2차' : input19, '스트레치_하강_시작' : input20, '스트레치_상승_시작' : input21,
                   '장전시간' : input22, '배압' : input23, '사출시간' : input24, 'N' : input25, 'F' : input26, 'M' : input27, 'R' : input28,
                   '블록_S' : input29, '블록_1' : input30, '블록_2' : input31, '블록_3' : input32, '블록_4' : input33, '노즐_1' : input34, '노즐_2' : input35,
                   '노즐_3' : input36, '노즐_4' : input37, '노즐_5' : input38, '노즐_6' : input39, '노즐_7' : input40, '노즐_7' : input41, '노즐_8' : input42,
                   '노즐_9' : input43, '노즐_10' : input44, '타이머_M2' : input45, '타이머_M1' : input46, '위치_p-v' : input47, '위치_3-2' : input48, '위치_2-1' : input49, '위치_샷크기' : input50,
                   'MPA_5' : input51, 'MPA_4' : input52, 'MPA_3' : input53, 'MPA_2' : input54, 'MPA_1' : input55, '속도_%_5' : input56, '속도_%_4' : input57, '속도_%_3' : input58, '속도_%_2' : input59, '속도_%_1' : input60,
                   'PNI' : input61, '샷크기' : input62, 'MPA_다시흡입위치' : input63, '압력_MPA_2' : input64, '압력_MPA_1' : input65, '속도%2' : input66, '속도%1' : input67
                   }
        data = data.append(new_row, ignore_index=True)
        save_data(data)
        st.success('Saved')



if __name__ == '__main__':
    main()
