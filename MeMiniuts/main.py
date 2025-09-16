import subprocess
import sys

def run_streamlit():
    # Run the Streamlit command to start the app
    # command1 = [r"F:\VS Workspace\pyenv\Scripts\activate"]
    command = ["streamlit", "run", r'f:\VS Workspace\AI-and-ML\MeMiniuts\src\app.py']
    try:
        # subprocess.run(command1, check=True)
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_streamlit()
