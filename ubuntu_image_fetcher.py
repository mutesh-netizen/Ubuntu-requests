import os
import requests
from urllib.parse import urlparse
import sys

def fetch_image():
    url = input("Please enter the URL of the image to fetch: ").strip()

    # Validate URL scheme
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Error: URL must start with http:// or https://")
        return

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Extract filename from URL path
        path = urlparse(url).path
        filename = os.path.basename(path)
        
        # If no filename or it doesn't have an image extension, generate one
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']
        if not filename or not any(filename.lower().endswith(ext) for ext in valid_extensions):
            filename = "fetched_image"

            # Try to get extension from content-type header if possible
            content_type = response.headers.get('Content-Type', '')
            if 'image/jpeg' in content_type:
                filename += '.jpg'
            elif 'image/png' in content_type:
                filename += '.png'
            elif 'image/gif' in content_type:
                filename += '.gif'
            elif 'image/bmp' in content_type:
                filename += '.bmp'
            elif 'image/webp' in content_type:
                filename += '.webp'
            else:
                filename += '.img'  # fallback generic extension

        # Save the image file in binary mode
        file_path = os.path.join(save_dir, filename)
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"Image saved successfully to: {file_path}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the URL provided.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
    except Exception as e:
        print(f"Failed to save image due to: {e}")

if __name__ == "__main__":
    fetch_image()
