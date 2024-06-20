@echo off
REM Stock Data Scrapers

REM This repository contains two Python scripts for scraping stock data from Central Charts:
REM 1. `nasdaq_scraper.py`: Scrapes NASDAQ tickers and generates various plots.
REM 2. `multi_scraper.py`: Scrapes multiple stock lists and stores the data into an Excel file with multiple sheets.

REM Table of Contents
REM - Requirements
REM - Installation
REM - Usage
REM   - NASDAQ Scraper
REM   - Multi Scraper
REM - Project Structure
REM - Contributing
REM - License

REM Requirements
REM - Python 3.x
REM - Required Python packages (install via `requirements.txt`)

REM Installation

REM 1. Clone the repository:
echo Cloning the repository...
git clone https://github.com/yourusername/stock-data-scrapers.git
cd stock-data-scrapers

REM 2. Create a virtual environment and activate it:
echo Creating a virtual environment...
python -m venv venv
echo Activating the virtual environment...
REM On Windows, use the following command to activate
venv\Scripts\activate

REM 3. Install the required packages:
echo Installing required packages...
pip install -r requirements.txt

REM Usage

REM NASDAQ Scraper
REM The `nasdaq_scraper.py` script scrapes NASDAQ tickers and generates various plots.

REM 1. Open the `nasdaq_scraper.py` file and configure any necessary parameters.
REM 2. Run the script:
echo Running NASDAQ scraper...
python nasdaq_scraper.py

REM 3. The script will scrape NASDAQ tickers, generate plots, and save the data to `stock_data.csv`.

REM Multi Scraper
REM The `multi_scraper.py` script scrapes multiple stock lists from Central Charts and stores the data into an Excel file with multiple sheets.

REM 1. Open the `multi_scraper.py` file and configure any necessary parameters.
REM 2. Run the script:
echo Running multi scraper...
python multi_scraper.py

REM 3. The script will scrape data from multiple stock lists and save the data to `all_stock_data.xlsx`.

REM Project Structure
REM The structure of the project is as follows:
REM .
REM ├── nasdaq_scraper.py      # Script to scrape NASDAQ tickers and generate plots
REM ├── multi_scraper.py       # Script to scrape multiple stock lists
REM ├── requirements.txt       # List of required Python packages
REM ├── README.md              # This README file

REM Contributing
REM Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

REM License
REM This project is licensed under the MIT License.
