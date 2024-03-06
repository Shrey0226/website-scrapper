# Website-Scraper

Web Scraper is a Django project designed to scrape links from any given URL. It provides a user-friendly interface to input a URL, scrape its links, and display them neatly.

## Features

- Input a URL and scrape links from it.
- Display scraped links in a tabular format.
- User-friendly interface for easy interaction.
- Integration with Django framework for backend functionality.

## Requirements

- Python 3.x
- Django
- BeautifulSoup (for scraping HTML content)
- Requests (for fetching web pages)
- Bootstrap (for styling frontend)
- Other dependencies as listed in requirements.txt

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Shrey0226/website-scrapper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd web-scraper
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the web application at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Usage

1. Navigate to the web application in your browser.
2. Enter the URL you want to scrape in the provided input field.
3. Click on the "Submit" button to start scraping.
4. Scrape links from multiple URLs as needed.
5. Use the "Delete" button to remove unwanted links.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for any improvements or fixes you'd like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project is built using Django framework.
- It utilizes BeautifulSoup and Requests libraries for web scraping.
- Frontend styling is done using Bootstrap.

