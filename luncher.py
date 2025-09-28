import subprocess
import threading
import time
import webbrowser


def run_streamlit():
    # uruchamia streamlit jako osobny proces
    subprocess.Popen(["streamlit", "run", "app.py", "--server.headless=true"])

def open_browser():
    time.sleep(2)  # poczekaj aż serwer wstanie
    webbrowser.open("https://labmagazyn.streamlit.app/")

if __name__ == "__main__":
    threading.Thread(target=run_streamlit).start()
    threading.Thread(target=open_browser).start()
