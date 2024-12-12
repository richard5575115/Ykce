import streamlit as st
from streamlit_option_menu import option_menu
from mssql_class import ykcemssql   as sqlobj
# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
EXAMPLE_NO = 1




def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title=None,  # required
                options=["首頁", "相片分類情形", "統計查詢"],  # required
                icons= ["🌐", "📷", "🗺️"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
 

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Projects", "Contact"],  # required
            icons=["house", "book", "envelope"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected
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

selected = streamlit_menu(example=EXAMPLE_NO)
 

if selected == "首頁":
    st.title(f"You have selected {selected}")
if selected == "相片分類情形":
    st.title(f"You have selected {selected}")
if selected == "統計查詢":
    st.title(f"You have selected {selected}")
