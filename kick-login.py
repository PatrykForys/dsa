from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from colorama import Fore, Style
from seleniumbase import Driver
from time import sleep
import re

channel_url = "FaceitBOT"
message_mode = int(input("Message Mod (0- Off | 1- Constant Message | 2- Static Message): "))

if message_mode == 1:
    const_message = input("Input Message: ")

username = "extazzy997"
password = "12121221As!"

def login_kick():
    driver_kick = Driver(
        uc=True,
        chromium_arg="--mute-audio",
        block_images=True,
        ad_block=True,
        headless=False
    )
    driver_kick.maximize_window()
    try:
        driver_kick.open(f"https://kick.com/{channel_url}")
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Error opening Kick.com: {e}")
        driver_kick.quit()
        return
    driver_kick.implicitly_wait(10)

    login_button = WebDriverWait(driver_kick, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Log In') or contains(., 'Login')]"))
    )
    login_button.click()
    
    sleep(1)

    try:
        driver_kick.find_element(By.CSS_SELECTOR, "input[name='emailOrUsername']").send_keys(username)
        driver_kick.find_element(By.CSS_SELECTOR, "input[name='password']").send_keys(password)
        
        login_submit_button = WebDriverWait(driver_kick, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form button[type='submit']"))
        )
        login_submit_button.click()
        
        # Check for 2FA/security code input field
        try:
            security_code_input = WebDriverWait(driver_kick, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='code']"))
            )
            security_code = input(f"{Fore.CYAN}[?] {Style.RESET_ALL}Please enter the 6-digit security code: ")
            security_code_input.send_keys(security_code)
            
            # Assuming there's a submit button for the security code as well
            security_code_submit_button = WebDriverWait(driver_kick, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "form button[type='submit']"))
            )
            security_code_submit_button.click()
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Security code entered.")
        except Exception as e:
            print(f"{Fore.LIGHTYELLOW_EX}[!] {Style.RESET_ALL}No security code prompt found or error entering code: {e}")

        sleep(5)

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Error during login form interaction: {e}")
        # driver_kick.quit()
        return

    # Removed email verification logic

    print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} login successfully.")
    
    # Çerez Kabul
    try:
        accept_button = WebDriverWait(driver_kick, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kabul Et']"))
        )
        accept_button.click()
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} accepted cookies.")
    except Exception:
        print(f"{Fore.LIGHTYELLOW_EX}[+] {Style.RESET_ALL}{username} cannot accepted cookies.")
    
    sleep(1)
    
    # Chat Kural
    try:
        message_button = WebDriverWait(driver_kick, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Kabul ediyorum']"))
        )
        message_button.click()
        print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} chat rules accepted successfully.")
    except Exception:
        print(f"{Fore.LIGHTYELLOW_EX}[!] {Style.RESET_ALL}{username} chat rules not accepted.")
    
    # Mesaj gönderme döngüsü
    while True:
        if message_mode == 0:
            break
        elif message_mode == 2:
            user_message = input("Enter message to send (or 'exit' to quit): ")
            if user_message.lower() == 'exit':
                break
            message_text = user_message
        elif message_mode == 1:
            message_text = const_message
            print(f"Sending constant message: {message_text}")
            # Optionally sleep or add condition to send repeatedly
            sleep(5)  # Adjust delay as needed
        
        try:
            message_input = WebDriverWait(driver_kick, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.editor-input[data-input='true']"))
            )
            message_input.send_keys(message_text)

            send_button = WebDriverWait(driver_kick, 10).until(
                EC.element_to_be_clickable((By.ID, 'send-message-button'))
            )
            send_button.click()
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}{username} message sent successfully.")
        except Exception as e:
            print(f"{Fore.LIGHTYELLOW_EX}[!] {Style.RESET_ALL}{username} message not sent: {e}")

    # driver_kick.quit()

def main():
    try:
        login_kick()
    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Error: {e}")

if __name__ == "__main__":
    main()