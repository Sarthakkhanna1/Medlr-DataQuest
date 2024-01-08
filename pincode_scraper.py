from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
import time

def get_medicine_info(url, pincode):
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode (without UI)
    options.add_argument("--disable-gpu")  # Disable GPU acceleration for headless mode
    options.add_argument("--window-size=1920x1080")  # Set window size for headless mode

    # Create a Chrome webdriver
    service = ChromeService("path/to/chromedriver")  # Set the path to your chromedriver executable
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Navigate to the provided URL
        driver.get(url)
        time.sleep(5)  # Introduce a delay to ensure the page loads

        # Find and interact with elements to get medicine information
        availability_element = driver.find_element(By.XPATH, "//span[@class='sc-16b9dsl-3 cWnqVi']")
        delivery_date_element = driver.find_element(By.XPATH, "//span[@class='sc-16b9dsl-2 fUJFxx']")

        availability = availability_element.text.strip()
        delivery_date = delivery_date_element.text.strip()

        # Check medicine availability based on pincode
        if check_pincode_availability(availability, pincode):
            print(f"The medicine is available in your area with delivery on {delivery_date}.")
        else:
            print("The medicine is not available for delivery in your area.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # Close the browser
        driver.quit()

def check_pincode_availability(availability, pincode):
    # Implement logic to check if the medicine is available based on the pincode
    # You may need to parse the availability text and compare it with the provided pincode
    return pincode in availability

# Example usage:
url = input("Enter the URL of the medicine on Tata 1mg: ")
pincode = input("Enter your pincode: ")

start_time = time.time()
get_medicine_info(url, pincode)
end_time = time.time()

execution_time = end_time - start_time
print(f"Execution time: {execution_time:.2f} seconds.")
