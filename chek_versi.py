import os

versi = '1.26.0, 1.27.0, 1.27.1, 1.27.2, 1.28.0, 1.28.1, 1.28.2, 1.29.0, 1.30.0, 1.31.0, 1.31.1, 1.32.0, 1.32.1, 1.32.2rc1, 1.32.2, 1.33.0, 1.34.0, 1.35.0'

versi = versi.split(',')


for i in range(9999):
    versi = versi[i]
    print(versi)

    try:
        os.system(f'pip install streamlit=={versi}')
    except:
        pass

    try:
        os.system('python -m streamlit run streamlit_app.py')
    except:
        continue
    else:
        break