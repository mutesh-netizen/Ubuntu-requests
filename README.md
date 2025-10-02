# Ubuntu-Inspired Image Fetcher

## Overview

This Python script embodies the spirit of **Ubuntu** — "I am because we are" — by connecting to the global web community to respectfully fetch and organize shared images for later appreciation.

The script prompts the user for an image URL, downloads the image, and saves it in a dedicated folder while handling errors gracefully.

---

## Features

- **Fetch images** from any valid URL provided by the user.
- **Creates a directory** called `Fetched_Images` if it doesn’t exist to organize downloaded images.
- **Handles errors gracefully** such as HTTP errors, connection problems, and invalid URLs.
- **Extracts the filename** from the URL or intelligently generates one based on the content type.
- Saves images in **binary mode** to preserve file integrity.

---

## Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/) library

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Ubuntu_Requests.git
   cd Ubuntu_Requests
````

2. Install required Python packages:

   ```bash
   pip install requests
   ```

---

## Usage

Run the Python script:

```bash
python ubuntu_image_fetcher.py
```

You will be prompted to enter an image URL. After input, the image will be downloaded and saved in the `Fetched_Images` directory.

---

## Example

```plaintext
Please enter the URL of the image to fetch: https://example.com/images/sample.jpg
Image saved successfully to: Fetched_Images/sample.jpg
```

---

## Error Handling

The program gracefully handles:

* Invalid URLs (not starting with http/https)
* HTTP errors (404, 500, etc.)
* Connection issues and timeouts
* Unexpected errors without crashing

---

## Ubuntu Principles Implemented

* **Community**: Connects to the global web to fetch shared images.
* **Respect**: Handles failures and errors gracefully without abrupt crashes.
* **Sharing**: Organizes images neatly for easy access and further sharing.
* **Practicality**: Provides a simple, useful tool for downloading and organizing images.

---

## License

This project is for academic use only.

---

## Contact

For questions or feedback, please contact:
newtonmutembei047@gmail.com



If you want, I can help you customize it with your GitHub repo URL and your contact details!
```
