import json



def login(st,make_hashes,login_user,check_hashes,cache,create_usertable,ws,wb,view_all_users,pd):

    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        st.subheader("LOGIN GENRE")
        pass
    with col3:
        pass

    username = st.text_input("User Name")
    password = st.text_input("Password",type='password')

    if st.button("Login"):

        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))
        if result:

            # save cache login
            a = open(f'history.json')
            data = json.load(a)
            x = cache
            y = 'True'
            data[x] = y
            b = open(f'history.json', 'w')
            json.dump(data,b)
            b.close()
            create_usertable()

            import show_database as sd
            sd.sd(st,ws,wb,view_all_users,pd,cache)

def signup(st,create_usertable):
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
    code = st.text_input('CODE VERIFIKATOR')

    if st.button("Signup"):
        if code == '2801':
            create_usertable()
            create_usertable(new_user,create_usertable(new_password))
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
        else:
            st.warning('[+] CODE salah , mohon hubungi developer', icon="⚠️")