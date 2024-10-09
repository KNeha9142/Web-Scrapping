# NSE 52 Weeks High Web Scraping Project

This project involves web scraping stock data for companies listed on the **National Stock Exchange (NSE)** that have reached their 52-week highs. Using **Python** and libraries like `requests` and `BeautifulSoup`, the project collects, processes, and analyzes real-time stock market data. Below is a step-by-step breakdown of the entire workflow.

### Steps:

1. **Web Scraping Setup**:
   The project begins by setting up a web scraping environment using Python’s **requests** library to make HTTP requests and retrieve the HTML content of the target website. **BeautifulSoup** is then used to parse this HTML data. A specific financial website was selected, focusing on the page that lists the 52-week high stocks of NSE-listed companies. This process ensures the retrieval of dynamic and updated financial data in a structured format.

2. **Data Extraction**:
   Once the HTML is parsed, relevant stock information is extracted. This includes identifying HTML tags and classes containing key data like company names, stock prices, 52-week highs, and percentage changes. By isolating these tags, the project efficiently collects and structures data into a Python dictionary. Special attention is given to correctly handle dynamic content and data inconsistencies such as empty fields.

3. **Data Cleaning**:
   After extraction, the raw data often contains unwanted characters like newline symbols or excess spaces, and may have missing or incomplete entries. The project applies **pandas** functions to clean the data by removing unnecessary elements, formatting columns (e.g., removing currency symbols), and ensuring consistency across all fields. Any missing values are handled to ensure the dataset is ready for analysis, and data types are converted where necessary (e.g., from strings to numeric values).

4. **Data Analysis**:
   The cleaned data is loaded into a **pandas DataFrame** for structured analysis. Descriptive statistics are performed to gain insights into stock performance, identifying key trends such as the most volatile stocks or those with the highest gains. This analysis includes grouping data by industry (if available), calculating averages, and sorting companies based on their stock price movements. The goal is to uncover trends that may indicate market opportunities or risks.

5. **Exporting Data**:
   Once analysis is complete, the processed data is saved in a CSV format using **pandas**' `to_csv` function. This makes the dataset available for future analysis or visualization. The export feature ensures that the data can be shared or reused in other tools like Excel, Tableau, or Power BI, enabling further exploration or reporting. This step finalizes the project, making the results accessible beyond the notebook environment.

### Key Libraries and Tools:
- **requests**: To send HTTP requests and fetch web page content.
- **BeautifulSoup**: For parsing HTML and extracting specific elements.
- **pandas**: For data cleaning, manipulation, and analysis.
- **NumPy**: For numerical operations, if needed.

This project showcases my ability to perform web scraping, clean data from financial information. It reflects skills in automation, data processing, and real-world data handling.
