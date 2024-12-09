import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    # Define regex pattern to match the src attribute of an iframe with a YouTube embed URL
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'

    # Search for the pattern in the provided HTML string
    match = re.search(pattern, s)

    # If a match is found, construct the short URL using the captured group
    if match:
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"

    # Return None if no YouTube URL is found in the HTML
    return None

if __name__ == "__main__":
    main()
