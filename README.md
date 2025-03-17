# Amazon Test Case Study

This project contains automated tests for Amazon using Selenium WebDriver with Python and Behave.

## Prerequisites

- Python 3.8 or higher
- Chrome browser
- Git
(VPN - country US if you want all tests to pass)

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd Test-Case-Study-Amazon
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Unix/MacOS
# or
.\venv\Scripts\activate  # For Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download ChromeDriver:
```bash
cd drivers
chmod +x download_drivers.sh
./download_drivers.sh
```

This script will download the appropriate ChromeDriver version for your operating system:
- Windows: `drivers/windows/chromedriver-win32`
- Linux: `drivers/linux/chromedriver-linux64`
- MacOS: `drivers/macos/chromedriver-mac-arm64`

## Project Structure

```
Test-Case-Study-Amazon/
├── drivers/                # ChromeDriver executables
├── drivers/download_drivers.sh    # Driver download script
├── features/              
│   ├── environment.py     # Behave environment setup
│   ├── steps/             # Step definitions
│   └── *.feature   
├── pages/        
│   ├── __init__.py    
│   ├── amazon_home.py    
|   ├── base.py    
|   ├── cart.py         
│   └── search_page.py 
└── requirements.txt       # Python dependencies
```

## Running Tests

To run all tests:
```bash
behave
```

To run all tests and generate allure reports:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/ features
```

To show allure reports:
```bash
allure serve reports/
```

To run specific tags:
```bash
behave features --tags=your_tag
```
## Notes

- The tests will automatically create and clean up a `total_prods.csv` file during execution
- ChromeDriver is automatically configured based on your operating system
- Browser window will be maximized during test execution

## Troubleshooting

1. If you get ChromeDriver errors:
   - Ensure the download_drivers.sh script has been executed
   - Verify the driver version matches your Chrome browser version
   - Check if the driver has executable permissions

2. If tests fail to start:
   - Verify your Chrome browser is up to date
   - Ensure you're running from the project root directory

