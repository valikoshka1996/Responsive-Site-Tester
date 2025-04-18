# 🌐 Responsive Tester

A web-based tool built with Flask that captures screenshots of a given website URL across multiple screen sizes (mobile, tablet, laptop, desktop) using Selenium, and optionally analyzes the page structure. Screenshots are automatically cleaned up when they exceed a certain disk space limit.
![screen1](https://github.com/user-attachments/assets/03228ce9-7b1c-4daa-b520-bde45591015b)
![screen2](https://github.com/user-attachments/assets/9561fdef-fb33-46a3-a20b-47a5525c7cc1)

## 📸 Features

- Capture screenshots of any webpage in 4 device viewports.
- Responsive device emulation: Mobile, Tablet, Laptop, Desktop.
- Temporary file management — old screenshots are removed when they exceed 10MB in total.
- Simple, clean HTML interface.
- Easy deployment via Flask.

---

## ⚙️ Requirements

Ensure the following are installed:

- **Python 3.8+**
- **Google Chrome Browser**
- **ChromeDriver** *(automatically installed via `chromedriver-autoinstaller`)*
- **pip** for installing dependencies

---

## 🧰 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/valikoshka1996/Responsive-Site-Tester.git
cd responsive-tester
```

2. **(Optional) Create a virtual environment**:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

### `requirements.txt` example:

```txt
Flask
selenium
chromedriver-autoinstaller
```

---

## 🚀 Running the App

Once everything is set up, run the app:

```bash
python app.py
```

Visit the app in your browser at:

```
http://localhost:5021/
```

> By default, the app listens on host `45.129.99.27` and port `5021`. You can change this in `app.py`.

---

## 📁 Project Structure

```
responsive-tester/
│
├── app.py                     # Main Flask application
├── requirements.txt
│
├── static/
│   └── screenshots/           # Folder for generated screenshots (auto-managed)
│
├── templates/
│   ├── index.html             # Home form for URL input
│   └── result.html            # Screenshot display page
│
└── utils/
    ├── screenshot.py          # Logic for capturing screenshots using Selenium
    └── analyzer.py            # (Optional) Analysis logic of the webpage
```

---

## 🧹 Screenshot Management

The app automatically removes all files from the `static/screenshots` folder if its total size exceeds **10MB**. This ensures the server isn't flooded with leftover images.

---

## 🛠 Troubleshooting

- **Chrome not found?**
  Ensure Google Chrome is installed and available in your system PATH.

- **ChromeDriver mismatch?**
  The `chromedriver-autoinstaller` handles this automatically, but if it fails, update Chrome to the latest version.

---

## 🛡 Security Note

This app allows users to enter arbitrary URLs — make sure to sanitize input and potentially sandbox execution if deploying publicly.

---

## 📃 License

MIT License — free to use and modify.

---

Let me know if you'd like me to generate the `requirements.txt` content or anything else to go with this!
