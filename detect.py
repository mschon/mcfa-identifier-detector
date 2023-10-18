from selenium import webdriver
import csv

# Read URLs from a separate .txt file
with open("urls_to_check.txt", "r") as file:
    urls_to_check = file.read().splitlines()

string_to_check = "Paid for by".lower()

# Initialize a WebDriver instance (e.g., Chrome)
driver = webdriver.Chrome()

results = []

print("-------")
print(f"'{string_to_check}' results: ")
print("-------")

try:
    for url in urls_to_check:
        # Navigate to the URL
        driver.get(url)

        # Get the page source (i.e., the HTML content of the page)
        page_source = driver.page_source.lower()

        # Check if string_to_check appears anywhere in the page source
        if string_to_check in page_source:
            print(f"found on {url}")
            result = "found"
        else:
            print(f"not found on {url}")
            result = "not found"
        results.append((result, url))

finally:
    # Close the browser window
    driver.quit()

# Write the results to a CSV file
with open("results.csv", "w", newline="") as csvfile:
    csv_writer = csv.writer(csvfile)
    # Write column headers
    csv_writer.writerow(["result", "url"])
    # Write results for each URL
    csv_writer.writerows(results) 
