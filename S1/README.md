# Custom Screenshot Capture Chrome Extension

A Chrome extension that allows you to capture screenshots of web pages with various options.

## Features

- Capture visible area of the current tab
- Capture full page screenshot
- Capture custom selection area
- Options to include/exclude scrollbar and cursor
- Save screenshots with timestamp

## Installation

1. Download or clone this repository
2. Open Chrome and go to `chrome://extensions/`
3. Enable "Developer mode" in the top right corner
4. Click "Load unpacked" and select the extension directory

## Usage

1. Click the extension icon in your Chrome toolbar
2. Choose one of the following options:
   - "Capture Visible Area": Captures the currently visible portion of the page
   - "Capture Full Page": Captures the entire webpage, including scrolled content
   - "Capture Selection": Allows you to select a specific area of the page to capture

3. Configure options:
   - "Include Scrollbar": Toggle whether to include the scrollbar in the screenshot
   - "Show Cursor": Toggle whether to include the mouse cursor in the screenshot

4. The screenshot will be automatically downloaded with a timestamp in the filename

## Development

The extension is built using:
- Manifest V3
- Chrome Extension APIs
- Vanilla JavaScript

## Files Structure

- `manifest.json`: Extension configuration
- `popup.html`: Extension popup interface
- `popup.js`: Popup logic
- `background.js`: Background script for screenshot functionality
- `selection.js`: Area selection functionality
- `styles.css`: Popup styling

## License

MIT License 