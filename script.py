import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import random
import tkinter as tk
from tkinter import messagebox
import pickle
import os

# Function to save cookies to a file
def save_cookies(driver, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

# Function to load cookies from a file
def load_cookies(driver, file_path):
    with open(file_path, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

# Function to perform Bing searches
def perform_search(driver, term):
    try:
        driver.get("https://www.bing.com")
        time.sleep(random.uniform(2, 10))  # Wait for the page to load
        
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        
        # Type each character with a delay
        for char in term:
            search_box.send_keys(char)
            time.sleep(random.uniform(0.001, 0.01))  # Random delay between 1ms and 100ms
            
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(3, 7))  # Wait for search results to load
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to start the search process
def start_search(chromedriver_path, search_limit, cookies_path):
    try:
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # Set up the Chrome WebDriver service
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(20)

        # Check if cookies file exists
        if os.path.exists(cookies_path):
            driver.get("https://www.bing.com")
            load_cookies(driver, cookies_path)
            driver.refresh()
        else:
            # Prompt user to log in manually
            driver.get("https://login.live.com/")
            messagebox.showinfo("Login", "Please log in manually and then close the browser window.")
            save_cookies(driver, cookies_path)
            messagebox.showinfo("Success", "Cookies saved successfully. Please restart the script.")

            driver.quit()
            return

        # Read search terms from CSV file
        search_terms_df = pd.read_csv('search_terms.csv')
        search_terms = search_terms_df['term'].tolist()

        # Shuffle the list of search terms to randomize the order
        random.shuffle(search_terms)

        # Limit the number of searches
        search_limit = int(search_limit)

        # Loop through search terms with a limit
        for count, term in enumerate(search_terms):
            if count >= search_limit:
                break
            perform_search(driver, term)

        # Close the browser
        driver.quit()
        messagebox.showinfo("Success", "Searches completed successfully.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
    finally:
        root.quit()
        root.destroy()

# Function to start the process from GUI and close the GUI window
def start_from_gui():
    chromedriver_path = entry_path.get()
    search_limit = entry_limit.get()
    cookies_path = 'cookies.pkl'
    if chromedriver_path and search_limit.isdigit():
        root.withdraw()  # Hide the GUI window
        start_search(chromedriver_path, search_limit, cookies_path)
    else:
        messagebox.showerror("Error", "Please enter a valid ChromeDriver path and number of searches.")

# Create the GUI application
root = tk.Tk()
root.title("Bing Rewards Automation")

# Create a label and entry to input the ChromeDriver path
label_path = tk.Label(root, text="Enter your ChromeDriver path:")
label_path.pack(pady=10)

entry_path = tk.Entry(root, width=50)
entry_path.pack(padx=20, pady=10)  # Add padding on the left and right

# Create a label and entry to input the number of searches
label_limit = tk.Label(root, text="Enter the number of searches:")
label_limit.pack(pady=10)

entry_limit = tk.Entry(root, width=20)
entry_limit.pack(padx=20, pady=10)  # Add padding on the left and right

# Create a button to start the process
start_button = tk.Button(root, text="Start", command=start_from_gui)
start_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
