gspread is a Python library for the Google Sheets API. This directory contains various utility python scripts for using gspread. Official documentation for gspread can be found [here](https://gspread.readthedocs.io/en/latest/)

# Authentication

Google Sheets API needs [authentication](https://gspread.readthedocs.io/en/latest/oauth2.html). The general steps for authentication are:

1. Log in to your Google account and create a new project on the [Google Developers Console](https://console.developers.google.com/cloud-resource-manager). Enable `Drive API` and `Sheets API`.

2. Go to `Credentials`. Create a `Service account`.

3. Using the created service account, add a key. Select JSON and save the file locally. You will use this file for authentication on your Python scripts using gspread.

4. Take note of the client e-mail on the Service account you created and share the sheet you want to edit to the client e-mail.