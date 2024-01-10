import subprocess
import time

def open_url_multiple_users(url, num_users=50, delay_seconds=5):
    for user_id in range(1, num_users + 1):
        print(f"Opening {url} for User {user_id}")
        subprocess.Popen(['python', '-m', 'webbrowser', url])
        time.sleep(delay_seconds)

if __name__ == "__main__":
    target_url = 'https://mihir-music.vercel.app/'
    open_url_multiple_users(target_url)
