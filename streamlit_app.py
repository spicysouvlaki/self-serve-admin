import streamlit as st
import requests as r


def get_mem():
    pass

def set_mem(mem_level):
    pass

def get_roles():
    pass

def set_roles(roles):
    pass

st.markdown("# App Memory Level")
app_url = st.text_input("App URL")
if app_url:
    current_mem_level = get_mem()
    st.write("Current memory level:", current_mem_level)

update_mem = st.checkbox("Check to update the memory level for this app")
if update_mem:
    desired_mem_level = st.selectbox("Desired memory level", ["Normal", "Medium", "High"])
    set_mem(desired_mem_level)

st.markdown("# User Roles")
user_id = st.text_input("Github login ID")
if user_id:
    current_roles = get_roles()
    st.write("Current roles:", current_roles)
update_roles = st.checkbox("Check to update the roles for this user")
if update_roles:
    desired_roles = st.multiselect("Select roles:", ["ROLE1", "ROLE2", "ROLE3"])
    set_roles(desired_roles)

