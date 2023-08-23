import multiprocessing
import time

def background_task():
    while True:
        print("Running in the background...")
        time.sleep(1)

if __name__ == '__main__':
    background_process = multiprocessing.Process(target=background_task)
    background_process.daemon = True  # Set the process as a daemon so it runs in the background
    background_process.start()

    # Main program continues while the background process runs
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input == 'exit':
            break
        # Handle other commands as needed
