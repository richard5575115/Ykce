import streamlit as st

from mssql_class import ykcemssql   as sqlobj
# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1





def filter_model(kind,class_name):
    cursor = conn.get_all_student_dataset(kind,class_name)
    items = [row["zoho_Teacher"] for row in cursor.fetchall()]
    return items
st.sidebar.title(" 育光校務維護")
st.logo('D:\python\Streamlit\Ykce_Crm\育光LOG圖.png',size="large",)
 
st.sidebar.subheader('員林園') 

conn = sqlobj()
#=======================================
cursor = conn.get_teacher_dataset('員林園')
items = [row["班級名稱"] for row in cursor.fetchall()]
s_teacher = st.sidebar.selectbox('班級：',items)
#=======================================

s_student = st.sidebar.selectbox('學生：',filter_model('員林園',s_teacher), index=None,placeholder="請選學生",)

