import streamlit as st
import requests
from requests.exceptions import HTTPError

# TODO
# - password
# - submit form
# ? API to get and Enum
# ? API for validation?

ROLES = ["ROLE_S4T", "FEATURE_PRIVATE_REPO", "FEATURE_SECRETS_BETA", "FEATURE_SPINDOWN", "FEATURE_PYTHON_VERSION"]
RESOURCES = ["NORMAL", "MEDIUM", "HIGH", "UNKNOWN"]

def get_resources(owner, repo, branch, main):
    try:
        r = requests.get(f"http://apps-manager:8500/http/get-resources")
        r.raise_for_status()
    except HTTPError as http_err:
        st.error(f'HTTP error: {http_err}')
        return None
    except Exception as err:
        st.error(f'Error: {err}')
        return None

    obj = r.json()
    st.write(obj)
    return None


def set_resources(owner, repo, branch, main, target):
    try:
        r = requests.post(f"http://apps-manager:8500/http/update-memory-limits", json={"owner": owner, "repository": repo, "branch": branch, "main_module": main, "target": 1})
        r.raise_for_status()
    except HTTPError as http_err:
        st.error(f'HTTP error: {http_err}')
    except Exception as err:
        st.error(f'Error: {err}')

def get_roles(user_id):
    try:
        r = requests.get(f"http://apps-manager:8500/http/get-user-roles/{user_id}")
        r.raise_for_status()
    except HTTPError as http_err:
        st.error(f'HTTP error: {http_err}')
        return None
    except Exception as err:
        st.error(f'Error: {err}')
        return None

    obj = r.json()
    if "roles" in obj:
        return obj["roles"]
    return None

def add_role(user_id, role):
    try:
        r = requests.post(f"http://apps-manager:8500/http/add-user-role", json={'github_user_id': user_id, "permission": role})
        r.raise_for_status()
    except HTTPError as http_err:
        st.error(f'HTTP error: {http_err}')
    except Exception as err:
        st.error(f'Error: {err}')

def delete_role(user_id, role):
    try:
        r = requests.post(f"http://apps-manager:8500/http/delete-user-role", json={'github_user_id': user_id, "permission": role})
        r.raise_for_status()
    except HTTPError as http_err:
        st.error(f'HTTP error: {http_err}')
    except Exception as err:
        st.error(f'Error: {err}')

password = "ciao"

def main():
    st.markdown("# Manage the Resources for an App")
    col1, _, col2 = st.beta_columns((3, 1, 2))
    with col1:
        st.markdown("## Obtain Resources")
        app_owner = st.text_input("Owner")
        app_repo = st.text_input("Repository")
        app_branch = st.text_input("Branch")
        app_main = st.text_input("Main File Path")
    current_resources_level = None
    query_resources = col1.button("Query")
    if query_resources and app_owner and app_repo and app_branch and app_main:
        current_resources_level = get_resources(app_owner, app_repo, app_branch, app_main)
    with col2:
        st.markdown(f"**Current resource level:**")
        st.markdown(f"{current_resources_level}")

    col1, col2 = st.beta_columns((1,  1))
    col1.markdown("## Set Resources")
    desired_resources_level = col1.selectbox("Desired resource level", RESOURCES)
    update_resources = col1.button("Update")
    if update_resources and app_owner and app_repo and app_branch and app_main:
        set_resources(app_owner, app_repo, app_branch, app_main, desired_resources_level)

    st.markdown("# Manage User Roles")
    col1, _, col2 = st.beta_columns((3, 1, 2))
    col1.markdown("## Query User Roles")
    user_id = col1.text_input("Enter the Github login ID for the user")
    query_roles = col1.button("Query")
    current_roles = None
    if query_roles and user_id:
        current_roles = get_roles(user_id)
    col2.markdown("**Current roles:**")
    col2.markdown(f"{current_roles}")

    col1, col2 = st.beta_columns((1,  1))
    col1.markdown("## Update User Roles")
    user_id = col1.text_input("Enter the Github login ID for the user", key=1)
    role_name = col2.selectbox("Select role:", ROLES)
    action = col2.selectbox("Action", ["Add", "Delete"], index=0)
    upate_roles = col2.button("Query")
    result = col2.empty()
    if update_roles and user_id and action == "Add":
        add_role(user_id, role_name)
        result.markdown("Role Added")
    elif update_roles and user_id and action == "Delete":
        delete_role(user_id, role_name)
        result.markdown("Role removed")


st.write("TEST: the password is ciao")
entered_pwd = st.text_input("Password", type="password")

if entered_pwd == "":
    pass
elif entered_pwd == password:
    main()
else:
    st.error("Not authenticated. Enter the correct password.")


