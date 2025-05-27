import streamlit as st
from datetime import datetime, timedelta
#import pyperclip

# 用来处理日期格式
def parse_date(text):
    text = text.strip()
    for sep in ['.', '-', '/']:
        try:
            return datetime.strptime(text, f"%Y{sep}%m{sep}%d")
        except:
            continue
    return None

# Streamlit 界面
st.title("日期加减计算器")

st.markdown("### 请输入：")
date_input = st.text_input("起始日期（例如：2024.01.01）", "")
op_box = st.selectbox("选择操作符：", ["+", "-"])
day_input = st.text_input("天数（例如：130）", "")

# 按下按钮进行计算
if st.button("计算"):
    if not date_input or not day_input:
        st.error("请输入完整的日期和天数！")
    else:
        try:
            base_date = parse_date(date_input)
            days = int(day_input)
            if not base_date:
                raise ValueError("日期解析失败")
        except:
            st.error("请输入正确格式的日期和天数！")
        else:
            # 计算结果
            result_date = base_date + timedelta(days=days) if op_box == "+" else base_date - timedelta(days=days)
            weekday_str = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"][result_date.weekday()]
            
            result_string = f"计算结果为：{result_date.strftime('%Y.%m.%d')}（{weekday_str}）"
            st.success(result_string)

            # # 复制到剪贴板
            # pyperclip.copy(result_date.strftime("%Y.%m.%d"))
            # st.info(f"结果 {result_date.strftime('%Y.%m.%d')} 已复制到剪贴板")
