import subprocess
import sys

def run_streamlit():
    # Run the Streamlit command to start the app
    command = ["streamlit", "run", r'F:\VS Workspace\Python\MeMiniuts\src\main.py']
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_streamlit()
