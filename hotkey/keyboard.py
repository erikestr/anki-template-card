import time
import pyautogui
import keyboard

def auto_press_up_arrow():
    # Simulate pressing the up arrow key
    pyautogui.press('up')

if __name__ == "__main__":
    time.sleep(10)
    try:
        # Repeat the process 100 times
        for _ in range(100):
            # Give a 10-second delay
            time.sleep(0.3)
            auto_press_up_arrow()
            print(f"Processed { _ + 1 } times.")

        # Wait for the 'Escape' key press to finish the program
        print("Press 'Escape' to finish.")
        keyboard.wait('esc')
        print("Program finished.")

    except KeyboardInterrupt:
        print("Program interrupted.")