import os , sys
import streamlit as st

from utils.handlFile import save_files

# from transformers import EncoderDecoderModel, BertTokenizer
# from utils.modelConfig import modelConfigurations


# tocanizer = BertTokenizer.from_pretrained('bert-base-uncased')
# model = EncoderDecoderModel( "bert-base-uncased", "gpt2")

# Hide streamlit sidebar on startup
st.set_page_config(page_title="MeMiniut", 
                   page_icon=":robot_face:", 
                   layout="", 
                   initial_sidebar_state="collapsed")

class ApplicationState:
    def __init__(self):
        self.uploaded_files = None
        self.messages = []
        self.disable_upload_button = False
        
    
    def load_streamlit_app():
        try:
            flag=0
            st.sidebar.header("MeMiniut")

            st.title("Welcome to MeMiniut")
            st.header("Upload Section!!")
            

            # to add message dynamically on Screen
            def add_message():
                new_message = 'User:- '+ st.session_state.new_message
                if new_message:
                    st.session_state.messages.append(new_message)

            # Initialize session state for messages
            if 'messages' not in st.session_state:
                st.session_state.messages = []



            # file uploder for Files
            uploaded_files =st.file_uploader('Upload Files Here!',
                            type= ['mp4', 'mov'], accept_multiple_files=True)
            
            def perform_upload():
                if uploaded_files:
                    save_files(uploaded_files)
                    st.session_state.disable_upload_button = True
                else:
                    st.warning("Please select files to upload.", icon="⚠️")
            
            if uploaded_files:
                if 'disable_upload_button' not in st.session_state:
                    st.session_state.disable_upload_button= False
                st.sidebar.button(':green[Upload]', on_click=perform_upload, 
                                disabled= st.session_state.disable_upload_button)

                # To create Scrollable container to add chats in the container
                st.write("### Messages:")
                with st.container():
                    for msg in st.session_state.messages:
                        st.write(f"- {msg}")
                    
                global chat 
                
                chat = st.chat_input("Enter Your Message here!!!", key='new_message', 
                                                    on_submit=add_message)
                
            else:
                pass

            return uploaded_files 
        except Exception as e:
            print('Error occured: '+ str(e))







if __name__ == '__main__':
    # Load frontend Streamlit app
    uploaded_files = ApplicationState.load_streamlit_app()


    # modelConfigurations()
    # print(uploaded_files)