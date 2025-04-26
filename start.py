import subprocess
import os

def run_script(script_path):
    """
    运行指定的 Python 脚本。
    """
    try:
        result = subprocess.run(["python", script_path], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError as e:
        print(f"Error running script {script_path}: {e}")
        return False

def main():
    # 获取当前工作目录
    current_dir = os.getcwd()

    # 运行 screenshot.py
    screenshot = os.path.join(current_dir, "screenshot.py")
    print(f"Running {screenshot}...")
    if run_script(screenshot):
        print("screenshot.py completed successfully.")
    else:
        print("screenshot.py failed.")
        return

    # 运行 main.py
    main_script = os.path.join(current_dir, "main.py")
    print(f"Running {main_script}...")
    if run_script(main_script):
        print("main.py completed successfully.")
    else:
        print("main.py failed.")

if __name__ == "__main__":
    main()