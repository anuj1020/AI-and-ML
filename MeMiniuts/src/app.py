import os , sys
import streamlit as st

from utils.handlFile import getContentFromUploadedFiles, save_files


# Hide sidebar on startup
st.set_page_config(page_title="MeMiniut", 
                   page_icon=":robot_face:", 
                   layout="wide", 
                   initial_sidebar_state="collapsed")

class ApplicationState:
    def __init__(self):
        self.messages = []


    def load_streamlit_app():
        try:
            st.title('MeMiniut :robot_face:')
            # file uploder for Files
            uploaded_files = st.file_uploader('Upload Files Here!',
                            type= ['pdf','doc','docx'], accept_multiple_files=True)
            
            def perform_upload():
                if uploaded_files:
                    save_files(uploaded_files)
                    st.session_state.disable_upload_button = True
                    # uncomment the below line to enable button again after upload
                    st.session_state.disable_upload_button = False
                    st.success("Files Uploaded Successfully!!!", icon="✅")
                    st.balloons()
                else:
                    st.warning("Please select files to upload.", icon="⚠️")
            
            if uploaded_files:
                if 'disable_upload_button' not in st.session_state:
                    st.session_state.disable_upload_button= False
                if st.button(':green[Upload]', disabled= st.session_state.disable_upload_button):
                    with st.spinner('Uploading...'):
                        perform_upload()
                        content = getContentFromUploadedFiles(uploaded_files[0].name) 
                        print("Content Fetched from file!!")
                        st.write(content)




        except Exception as e:
            print('Error occured: '+ str(e))







if __name__ == '__main__':
    # Load frontend Streamlit app
    app = ApplicationState.load_streamlit_app()


    # modelConfigurations()
    # print(uploaded_files)