import os
import streamlit as st
import pandas as pd
import datetime

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9 = st.tabs(["4월","5월","6월","7월","8월","9월","10월","11월","12월"])


# 데이터를 저장할 파일의 경로를 지정합니다.
FILE_PATH = './data.csv'

def save_data(data):
    # 입력된 데이터를 CSV 파일에 저장합니다.
    if not os.path.exists(FILE_PATH):
        data.to_csv(FILE_PATH, index=False)
    else:
        existing_data = pd.read_csv(FILE_PATH)
        data = pd.concat([existing_data, data], ignore_index=True)
        data.to_csv(FILE_PATH, index=False)

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

    # 조건_네 번째 줄
    data = pd.DataFrame(columns=['바렐_N','바렐_F',"바렐_M","바렐_R"])
    
    # 조건_네 번째 줄
    col26, col27, col28, col29= st.columns(4)
    input26 = col26.text_input('바렐_N')
    input27 = col27.text_input('바렐_F')
    input28 = col28.text_input('바렐_M')
    input29 = col29.text_input('바렐_R')

    # 조건_다섯 번째 줄
    data = pd.DataFrame(columns=['핫트런너_블록_S','핫트런너_블록_1''핫트런너_블록_2''핫트런너_블록_3''핫트런너_블록_4'])
    
    # 조건_다섯 번째 줄
    col30, col31, col32, col33, col34= st.columns(5)
    input30 = col30.text_input('핫트런너_블록_S')
    input31 = col31.text_input('핫트런너_블록_1')
    input32 = col32.text_input('핫트런너_블록_2')
    input33 = col33.text_input('핫트런너_블록_3')
    input34 = col34.text_input('핫트런너_블록_4')

    # 조건_여섯 번째 줄
    data = pd.DataFrame(columns=['핫트런너_노즐_1','핫트런너_노즐_2','핫트런너_노즐_3','핫트런너_노즐_4','핫트런너_노즐_5'])
    
    # 조건_여섯 번째 줄
    col35, col36, col37, col38, col39= st.columns(5)
    input35 = col35.text_input('핫트런너_노즐_1')
    input36 = col36.text_input('핫트런너_노즐_2')
    input37 = col37.text_input('핫트런너_노즐_3')
    input38 = col38.text_input('핫트런너_노즐_4')
    input39 = col39.text_input('핫트런너_노즐_5')

    # 조건_일곱 번째 줄
    data = pd.DataFrame(columns=['사출제어_타이머_M2','사출제어_타이머_M1','사출제어_위치_p-v','사출제어_위치_3-2','사출제어_위치_2-1','사출제어_위치_샷크기'])
    
    # 조건_일곱 번째 줄
    col40, col41, col42, col43, col44, col45= st.columns(6)
    input40 = col40.text_input('사출제어_타이머_M2')
    input41 = col41.text_input('사출제어_타이머_M1')
    input42 = col42.text_input('사출제어_위치_p-v')
    input43 = col43.text_input('사출제어_위치_3-2')
    input44 = col44.text_input('사출제어_위지_2-1')
    input45 = col45.text_input('사출제어_위치_샷크기')

    # 조건_여덟 번째 줄
    data = pd.DataFrame(columns=['사출제어압력_MPA_5','사출제어_압력_MPA_4','사출제어_압력_MPA_3','사출제어_압력_MPA_2','사출제어_압력_MPA_1'])
    
    # 조건_여덟 번째 줄
    col46, col47, col48, col49, col50= st.columns(5)
    input46 = col46.text_input('사출제어압력_MPA_5')
    input47 = col47.text_input('사출제어압력_MPA_4')
    input48 = col48.text_input('사출제어압력_MPA_3')
    input49 = col49.text_input('사출제어압력_MPA_2')
    input50 = col50.text_input('사출제어압력_MPA_1')

    # 조건_아홉 번째 줄
    data = pd.DataFrame(columns=['사출제어_압력_속도_%_5','사출제어_압력_속도_%_4','사출제어_압력_속도_%_3','사출제어_압력_속도_%_2','사출제어_압력_속도_%_1'])
    
    # 조건_아홉 번째 줄
    col51, col52, col53, col54, col55= st.columns(5)
    input51 = col51.text_input('사출제어_압력_속도_%_5')
    input52 = col52.text_input('사출제어_압력_속도_%_4')
    input53 = col53.text_input('사출제어_압력_속도_%_3')
    input54 = col54.text_input('사출제어_압력_속도_%_2')
    input55 = col55.text_input('사출제어_압력_속도_%_1')

    # 조건_열 번째 줄
    data = pd.DataFrame(columns=['충전제어_PNI','충전제어_샷크기','충전제어_압력_MPA_다시흡입위치','충전제어_압력_MPA_2','충전제어_압력_MPA_1'])
    
    # 조건_열 번째 줄
    col56, col57, col58, col59, col60= st.columns(5)
    input56 = col56.text_input('충전제어_PNI')
    input57 = col57.text_input('충전제어_샷크기')
    input58 = col58.text_input('충전제어_압력_MPA_다시흡입위치')
    input59 = col59.text_input('충전제어_압렵_MPA_2')
    input60 = col60.text_input('충전제어_압력_MPA_1')

    # 조건_열한 번째 줄
    data = pd.DataFrame(columns=['충전제어_속도_%_2','충전제어_속도_%_1'])
    
    # 조건_열한 번째 줄
    col61, col62= st.columns(2)
    input61 = col61.text_input('충전제어_속도_%_2')
    input62 = col62.text_input('충전제어_속도_%_1')
    
    # "저장" 버튼을 클릭하면 입력한 데이터를 저장합니다.


    if st.button('저장'):
        new_row = {'날짜': input1, '기계': input2, '몰드': input3, '제품코드': input4, 'MB':input5}
        data = data.append(new_row, ignore_index=True)
        save_data(data)
        st.success('데이터가 저장되었습니다.')
        
if __name__ == '__main__':
    main()
