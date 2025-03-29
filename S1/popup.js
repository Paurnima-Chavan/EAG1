document.addEventListener('DOMContentLoaded', function() {
  const captureVisibleBtn = document.getElementById('captureVisible');
  const captureFullBtn = document.getElementById('captureFull');
  const captureSelectionBtn = document.getElementById('captureSelection');
  const includeScrollbarCheckbox = document.getElementById('includeScrollbar');
  const showCursorCheckbox = document.getElementById('showCursor');

  // Helper function to get current options
  function getOptions() {
    return {
      includeScrollbar: includeScrollbarCheckbox.checked,
      showCursor: showCursorCheckbox.checked
    };
  }

  // Capture visible area
  captureVisibleBtn.addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.runtime.sendMessage({
      action: 'captureVisible',
      tabId: tab.id,
      options: getOptions()
    });
  });

  // Capture full page
  captureFullBtn.addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.runtime.sendMessage({
      action: 'captureFull',
      tabId: tab.id,
      options: getOptions()
    });
  });

  // Capture selection
  captureSelectionBtn.addEventListener('click', async () => {
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    chrome.runtime.sendMessage({
      action: 'captureSelection',
      tabId: tab.id,
      options: getOptions()
    });
  });
}); 