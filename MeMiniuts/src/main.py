import os , sys
from transformers import EncoderDecoderModel, BertTokenizer
import streamlit as st

from modelConfig import modelConfigurations

chat = ''

# tocanizer = BertTokenizer.from_pretrained('bert-base-uncased')

# model = EncoderDecoderModel( "bert-base-uncased", "gpt2")
def load_streamlit_app():
    try:
        flag=0
        st.sidebar.header("MeMiniut")
        st.sidebar.header("Upload Section!!")
        
        # To save the files to storage
        def save_files():
            # flag=1
            save_dir = r"F:\VS Workspace\Python\MeMiniuts\uploads"
            os.makedirs(save_dir, exist_ok=True)  # Create the directory if it doesn't exist
            
            for uploaded_file in uploaded_files:
                file_path = os.path.join(save_dir, uploaded_file.name)

                # Save the file
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
            
            st.success(f"File saved to: {save_dir}", icon="✅")
            
            # to disable upload button
            st.session_state.disable_upload_button = True

        # to add message dynamically on Screen
        def add_message():
            new_message = 'User:- '+ st.session_state.new_message
            if new_message:
                st.session_state.messages.append(new_message)

        # Initialize session state for messages
        if 'messages' not in st.session_state:
            st.session_state.messages = []



        # file uploder for Files
        uploaded_files =st.sidebar.file_uploader('Upload Files Here!',
                        type= ['mp4', 'mov'], accept_multiple_files=True)
        
        
        if uploaded_files:
            if 'disable_upload_button' not in st.session_state:
                st.session_state.disable_upload_button= False
            st.sidebar.button(':green[Upload]', on_click=save_files, 
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
            st.title("Welcome to MeMiniut! Upload your files using the sidebar.")

        return uploaded_files 
    except Exception as e:
        print('Error occured: '+ str(e))







if __name__ == '__main__':
    # Load frontend Streamlit app
    uploaded_files = load_streamlit_app()
    save_dir = r"F:\VS Workspace\Python\MeMiniuts\uploads"
    # modelConfigurations()
    # print(uploaded_files)