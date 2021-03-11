import streamlit as st
import requests as r

# TODO
# - password
# - submit form
# ? API to get and Enum
# ? API for validation?

def get_resources(app_coords):
    return "RESOURCE_LEVEL_FAKE"

def set_resources(app_coords, resources_level):
    pass

def get_roles(user_id):
    return ["FAKE_ROLE1", "FAKE_ROLE2"]

def set_roles(user_id, roles):
    pass

st.markdown("# Manage the Resources for an App")
col1, _, col2 = st.beta_columns((3, 1, 2))
app_owner = col1.text_input("Owner")
app_repo = col1.text_input("Repository")
app_branch = col1.text_input("Branch")
app_main = col1.text_input("Main File Path")
current_resources_level = None
if app_owner and app_repo and app_branch and app_main:
    app_coords = (app_owner, app_repo, app_branch, app_main)
    current_resources_level = get_resources(app_coords)
col2.markdown(f"**Current resource level:**")
col2.markdown(f"{current_resources_level}")

col1, col2 = st.beta_columns((1,  1))
update_resources = col1.checkbox("Check to update the resource level for this app")
if update_resources:
    app_coords = (app_owner, app_repo, app_main)
    desired_resources_level = col2.selectbox("Desired resource level", ["Normal", "Medium", "High"])
    set_resources(app_coords, desired_resources_level)

st.markdown("# Manage User Roles")
col1, _, col2 = st.beta_columns((3, 1, 2))
user_id = col1.text_input("Enter the Github login ID for the user")
current_roles = None
if user_id:
    current_roles = get_roles(user_id)
col2.markdown("**Current roles:**")
col2.markdown(f"{current_roles}")

col1, col2 = st.beta_columns((1,  1))
update_roles = col1.checkbox("Check to update the roles for this user")
if update_roles:
    desired_roles = col2.multiselect("Select roles:", ["ROLE1", "ROLE2", "ROLE3"])
    set_roles(user_id, desired_roles)

