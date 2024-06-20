import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tenacity import retry, stop_after_attempt, wait_fixed

# this is the base URL of centralcharts
base_url = 'https://www.centralcharts.com/en/price-list-ranking/'
#in this list you can put every link you want from central charts 
list_options = {
    'US NASDAQ Stocks': 'ALL/asc/ts_19-us-nasdaq-stocks--qc_1-alphabetical-order?p=',
    'US NASDAQ OTCBB': 'ALL/asc/ts_76-chix-us-nasdaq-otcbb--qc_1-alphabetical-order?p='
}


@retry(stop=stop_after_attempt(5), wait=wait_fixed(5))
def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    return response

# Initialize a dictionary to store dataframes
dataframes = {}

# Iterate over each list option
for list_name, list_url in list_options.items():
    print(f'Scraping data for {list_name}...')
    all_pages_data = []
    
    # Scrape multiple pages (if applicable)
    for page_number in range(2, 10):  # Adjust range as needed
        page_url = base_url + list_url + str(page_number)
        print(f'Fetching URL: {page_url}')  # Debug statement to print the URL being fetched
        try:
            webpage = fetch_page(page_url)
            soup = bs(webpage.text, 'html.parser')
            
            # Check if the page contains a table
            stock_table = soup.find('table', class_='tabMini tabQuotes')
            if stock_table:
                tr_tag_list = stock_table.find_all('tr')
                
                # Extract header and data rows
                if not all_pages_data:
                    th_tag_list = stock_table.find_all('th')
                    headers = [th.text.strip() for th in th_tag_list]
                    all_pages_data.append(headers)
                
                for each_tr_tag in tr_tag_list[1:]:
                    td_tag_list = each_tr_tag.find_all('td')
                    row_values = [each_td_tag.text.strip() for each_td_tag in td_tag_list]
                    all_pages_data.append(row_values)
            else:
                print(f'No table found on page {page_number} for {list_name}')  # Debug statement
                break  # Stop if no more tables found
        except Exception as e:
            print(f'Error scraping page {page_number} of {list_name}: {e}')
            break

    # Create a dataframe for the current list
    if all_pages_data:
        df = pd.DataFrame(all_pages_data[1:], columns=all_pages_data[0])
        dataframes[list_name] = df
    else:
        print(f'No data found for {list_name}.')

# Save all dataframes to a single Excel file with multiple sheets
if dataframes:
    with pd.ExcelWriter('all_stock_data.xlsx') as writer:
        for list_name, df in dataframes.items():
            # Sanitize sheet names to avoid Excel issues
            sheet_name = list_name[:30].replace('/', '_')
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print('Data scraping and saving completed successfully.')
else:
    print('No data to save.')
