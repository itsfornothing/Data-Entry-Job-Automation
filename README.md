Zillow Data Scraper and Google Form Filler
Description
This Python script scrapes property listings from a mock Zillow page and automatically fills out a Google Form with the data. It uses BeautifulSoup to extract property information such as prices, addresses, and links from the Zillow page. Then, it utilizes Selenium to interact with a Google Form and submit the scraped data.

Requirements
Python 3.x
requests library
beautifulsoup4 library
selenium library
ChromeDriver (compatible with your version of Chrome)
Installation
Install Required Python Libraries:
Ensure you have the necessary Python libraries by running:

bash
Copy code
pip install requests beautifulsoup4 selenium
Download ChromeDriver:

Download the appropriate ChromeDriver version from ChromeDriver.
Ensure the chromedriver executable is in your PATH or specify its location in the script.
Usage
Run the Script:

Simply run the script using Python:
bash
Copy code
python zillow_form_filler.py
The script will scrape the Zillow Clone website and then proceed to automatically fill out a Google Form with the retrieved data.
Data Flow:

The script fetches the Zillow Clone page content.
It parses the content to extract property links, prices, and addresses.
The extracted data is then used to fill out a Google Form.
Code Breakdown
1. Web Scraping with BeautifulSoup:
The script sends a GET request to the Zillow Clone page to retrieve HTML data.
It then parses the HTML using BeautifulSoup to find property details:
Property links are extracted from <a> tags within div elements of the class StyledPropertyCardDataWrapper.
Prices and addresses are extracted from span and address tags, respectively.
2. Form Filling with Selenium:
Selenium WebDriver is used to open the Google Form and input the scraped data.
The script navigates through the form fields and enters the data, then submits the form.
3. Form Submission Loop:
The script loops through the scraped data, filling out the form for each property, and submits the form multiple times.
Notes
Google Sign-In Issues:
The script doesn't handle Google sign-in. Ensure that the Google Form used does not require sign-in or that the browser session is already authenticated.

Modifying the Script:

Update the URL in Zillow_url with the actual Zillow page if needed.
Adjust the XPaths in the Selenium part if the structure of the Google Form changes.
Disclaimer
This script is for educational purposes only. Ensure you comply with the terms of service of the websites you are scraping or interacting with.
