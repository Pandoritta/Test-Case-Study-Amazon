#!/bin/bash


#MacOS
curl -O https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/mac-arm64/chromedriver-mac-arm64.zip
unzip -o chromedriver-mac-arm64.zip -d macos/
chmod +x macos/chromedriver-mac-arm64
rm chromedriver-mac-arm64.zip

#Linux
curl -O https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/linux64/chromedriver-linux64.zip
unzip -o chromedriver-linux64.zip -d linux/
chmod +x linux/chromedriver-linux64
rm chromedriver-linux64.zip

#Windows
curl -O https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.88/win32/chromedriver-win32.zip
unzip -o chromedriver-win32.zip -d windows/
rm chromedriver-win32.zip

