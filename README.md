# Microsoft Bing Rewards Automation Script

## Introduction

This Python script automates the process of earning Microsoft Rewards points on Bing by performing everyday searches. By following these instructions, you'll be able to set up and run the script effortlessly, allowing you to redeem rewards with ease.

## Steps to Run the Script

### 1. Install Dependencies

Ensure you have the following Python libraries installed. You can install them using pip. Here's how to do it for both Windows and Mac:

**For Windows:**
```bash
pip install pandas selenium
```

### 2. Download Python and CSV File

Make sure you have Python installed on your system. Place the Python script and the required CSV file in the same directory.

### 3. Download Chromedriver

Download the ChromeDriver that matches the version of your Google Chrome browser from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads). Ensure the chromedriver executable is in a known location.

### 4. Register a Microsoft Rewards Account

If you don't already have a Microsoft Rewards account, register for one [here](https://account.microsoft.com/rewards/).

### 5. Run the Python Script

Run the Python script for the first time. A pop-up window will appear. Without closing the pop-up, log in to your Microsoft account. This step will generate the `cookies.pkl` and `state.json` files needed for subsequent runs.

### 6. Restart the Program

After generating the `cookies.pkl` and `state.json` files, restart the program and run the script again.

### 7. Specify Chromedriver Path and Number of Searches

When prompted, copy and paste the directory path to the `chromedriver.exe` file. The path should look something like this if it is in your Downloads folder:

```
\Users\user\Downloads\chromedriver-win64\chromedriver.exe
```

Input the number of searches you want the script to perform.

### 8. Enjoy Your Microsoft Rewards Points!

Sit back and let the script automate your Bing searches, earning you Microsoft Rewards points effortlessly.

By following these steps, you can streamline the process of earning rewards, allowing you to redeem them with minimal effort.

---
