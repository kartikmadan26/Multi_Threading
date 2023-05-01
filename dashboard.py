import streamlit as st
import os,sys,time,random as r,threading,multiprocessing
from streamlit.scriptrunner.script_run_context import add_script_run_ctx
# from streamlit.scriptrunner.script_run_context import add_report_ctx

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)
# def display(num,col):
#     with col:
#         text_element = st.text(num)
#         text_element.text(num)
def task(lb,ub,refreshtime,col):
    with col:
        mes="[ "+str(lb)+" , "+str(ub)+" ] "+" time = "+str(refreshtime)
        st.text(mes)
        
        message = "Hello, World!"
        text_element = st.text(message)
        while(1):
            num=r.randint(lb,ub)
        # text_element = st.text(num)
            text_element.text(num)
            # display(num,col)
            # print(num)
            # st.write(num)
            time.sleep(refreshtime)
        return
def main():
    # task(10,20,10)
    t1=threading.Thread(target=task,args=(10,20,10,col1))
    t2=threading.Thread(target=task,args=(-10,10,1,col2))
    t3=threading.Thread(target=task,args=(-100,0,5,col3))
    t4=threading.Thread(target=task,args=(0,20,8,col4))
    t5=threading.Thread(target=task,args=(-40,40,2,col5))
    t6=threading.Thread(target=task,args=(100,200,1,col6))
    add_script_run_ctx(t1)
    t1.start()
    add_script_run_ctx(t2)
    t2.start()
    add_script_run_ctx(t3)
    t3.start()
    add_script_run_ctx(t4)
    t4.start()
    add_script_run_ctx(t5)
    t5.start()
    add_script_run_ctx(t6)
    t6.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
main()