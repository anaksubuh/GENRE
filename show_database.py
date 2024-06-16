import json

def sd(st,ws,wb,pd,cache):

    #st.success("Logged In as {}".format(username))

    col1, col2, col3, col4, col5= st.columns(5)

    with col1:
        task = st.selectbox('Menu',["SUARA HATI","Analytics","Profiles"])
    with col5:
        if st.button('logout'):
            # save cache login
            a = open(f'history.json')
            data = json.load(a)
            x = cache
            y = 'False'
            data[x] = y
            b = open(f'history.json', 'w')
            json.dump(data,b)
            b.close()

    if task == "SUARA HATI":

        # ============== MAKE DATA TXT TO EXEL ==============#
        # Using readlines()
        file1 = open('cerita_global.txt', 'r' , encoding="utf8")
        Lines = file1.readlines()
        count = 0
        # Strips the newline character
        for line in Lines:
            count += 1
            linee = count
            data = (count, line.strip())
            data = str(data)
            tasta = ('IDENTITAS' if (count % 2 == 0) else 'CERITA')

            if tasta == 'CERITA':

                # data remove
                data = data.replace(f"({count}, 'Name : "," ")
                data = data.replace("age : "," ")
                data = data.replace("post date : "," ")
                data = data.replace("Hidden : "," ")
                data = data.replace("')"," ")
                data = data.split('|')
                #============== ==============#
                nama     = data[0]
                age      = data[1]
                postdate = data[2]
                hidden   = data[3]

                ws[f'A{count}'] = nama
                ws[f'B{count}'] = age
                ws[f'C{count}'] = postdate
                ws[f'D{count}'] = hidden

            if tasta == "IDENTITAS":
                data = data.replace(f"({count}, '"," ")
                data = data.replace("')"," ")
                data = str(data)
                cerita = data

                print(f'Name      : {nama}\nage       : {age}\npost date : {postdate}\nHidden    : {hidden}\ncerita    : {cerita}')
                print('')
                ws[f'F{count}'] = cerita

        wb.save('genre.csv')
        # ============== MAKE DATA TXT TO EXEL ==============#

        col1, col2, col3, col4, col5, col6= st.columns(6)
        with col1:
            st.info('Import All data user in csv : ', icon="ℹ️")
        with col2:
            with open("genre.csv", "rb") as file:
                btn = st.download_button(
                        label="DOWNLOAD genre.csv",
                        data=file,
                        file_name="genre.csv",
                        mime=""
                    )

        # reading database
        database = open('cerita_global.txt', 'r',encoding="utf8")
        count = 0
        # Using for loop
        for data in database:
            count += 1
            text = (str(data.strip()))
            ganjil_genap = ('genap' if (count % 2 == 0) else 'ganjil')
            if ganjil_genap == 'ganjil':
                col1, col2= st.columns(2)
                with col1:
                    st.success(text, icon="ℹ")
                    if text.count('Hidden : True'):
                        text = text.replace('200'or'404','')
                        status_hidden = True
                    if text.count('Hidden : False'):
                        status_hidden = False
                with col2:
                    st.info(f"Hidden : {status_hidden}")

            if ganjil_genap == 'genap':
                if status_hidden == True:
                    st.error(text, icon="🚨")
                else:
                    st.info(text, icon="ℹ️")
                st.warning('|'+'-'*60+'|')
            st.caption('')

    elif task == "Analytics":
        st.caption('BELUM ADA KONTEN')