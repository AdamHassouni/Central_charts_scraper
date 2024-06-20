# Stock Data Scrapers

This repository contains two Python scripts for scraping stock data from Central Charts:
1. `nasdaq_scraper.py`: Scrapes NASDAQ tickers and generates various plots.
2. `multi_scraper.py`: Scrapes multiple stock lists and stores the data into an Excel file with multiple sheets.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [NASDAQ Scraper](#nasdaq-scraper)
  - [Multi Scraper](#multi-scraper)

- [Contributing](#contributing)


## Requirements
- Python 3.x
- Required Python packages (install via `requirements.txt`)

## Installation

1. Clone the repository:

    ```sh
    echo Cloning the repository...
    git clone https://github.com/yourusername/stock-data-scrapers.git
    cd stock-data-scrapers
    ```

2. Create a virtual environment and activate it:

    ```sh
    echo Creating a virtual environment...
    python -m venv venv
    echo Activating the virtual environment...
    ```

    On Windows, use the following command to activate:
    ```sh
    venv\Scripts\activate
    ```

3. Install the required packages:

    ```sh
    echo Installing required packages...
    pip install -r requirements.txt
    ```

## Usage

### NASDAQ Scraper

The `nasdaq_scraper.py` script scrapes NASDAQ tickers and generates various plots.

1. Open the `nasdaq_scraper.py` file and configure any necessary parameters.
2. Run the script:

    ```sh
    echo Running NASDAQ scraper...
    python nasdaq_scraper.py
    ```

3. The script will scrape NASDAQ tickers, generate plots, and save the data to `stock_data.csv`.
   ![Figure_1](https://github.com/AdamHassouni/Central_charts_scraper/assets/122727246/f95668d3-22b9-43f5-abc6-2d82fd0881d4)

   ![Figure_5](https://github.com/AdamHassouni/Central_charts_scraper/assets/122727246/71dc0919-61f6-4ce5-8a36-2bc6c112ab64)

   ![Figure_3](https://github.com/AdamHassouni/Central_charts_scraper/assets/122727246/4df3fe58-52fa-4787-adbb-10361cd6c297)

   ![WhatsApp Image 2024-06-20 à 14 01 36_ba8e2f51](https://github.com/AdamHassouni/Central_charts_scraper/assets/122727246/0cf17cfa-bf7d-4284-bc36-392e494f28df)


### Multi Scraper



The `multi_scraper.py` script scrapes multiple stock lists from Central Charts and stores the data into an Excel file with multiple sheets.

1. Open the `multi_scraper.py` file and configure any necessary parameters.
2. Run the script:

    ```sh
    echo Running multi scraper...
    python multi_scraper.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
