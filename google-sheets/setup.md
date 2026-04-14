# Google Sheets API – Setup

Setup process for the Google Sheets chapter of *Automate the Boring Stuff with Python*.

---

## Dependencies

```bash
pip install ezsheets
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

## OAuth Credentials

### 1. Create a project on Google Cloud Console

- Go to [console.cloud.google.com](https://console.cloud.google.com)
- Create a new project
- Enable the **Google Sheets API** and **Google Drive API**

### 2. Configure OAuth consent screen

- Go to **Google Auth Platform → Branding** (current UI, 2025)
- Fill in the basic app information

### 3. Add an authorized test user

- Go to **Google Auth Platform → Audience**
- Scroll to the **Test users** section
- Add the email that will be used to authenticate

> ⚠️ Without this step, OAuth returns `403: access_denied`.

### 4. Download credentials

- Go to **Google Auth Platform → Clients**
- Create an OAuth 2.0 client of type **Desktop app**
- Download the generated JSON file
- Rename it to `credentials-sheets.json`
- Place it in the same folder as your script

---

## First Run

On the first script execution, the browser opens for OAuth authorization. After authorizing, a `token.json` file is generated locally — subsequent runs won't prompt for login again.