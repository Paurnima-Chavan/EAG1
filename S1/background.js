chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action.startsWith('capture')) {
    handleScreenshot(request);
  }
});

async function handleScreenshot(request) {
  const { action, tabId, options } = request;
  
  try {
    let screenshotData;
    
    switch (action) {
      case 'captureVisible':
        screenshotData = await captureVisibleArea(tabId, options);
        break;
      case 'captureFull':
        screenshotData = await captureFullPage(tabId, options);
        break;
      case 'captureSelection':
        screenshotData = await captureSelection(tabId, options);
        break;
    }

    if (screenshotData) {
      downloadScreenshot(screenshotData);
    }
  } catch (error) {
    console.error('Screenshot capture failed:', error);
  }
}

async function captureVisibleArea(tabId, options) {
  return await chrome.tabs.captureVisibleTab(null, {
    format: 'png'
  });
}

async function captureFullPage(tabId, options) {
  // Inject script to get full page dimensions
  const [{ result }] = await chrome.scripting.executeScript({
    target: { tabId },
    function: () => ({
      width: Math.max(
        document.documentElement.clientWidth,
        document.body.scrollWidth,
        document.documentElement.scrollWidth
      ),
      height: Math.max(
        document.documentElement.clientHeight,
        document.body.scrollHeight,
        document.documentElement.scrollHeight
      )
    })
  });

  // Capture the full page
  return await chrome.tabs.captureVisibleTab(null, {
    format: 'png',
    clip: {
      x: 0,
      y: 0,
      width: result.width,
      height: result.height
    }
  });
}

async function captureSelection(tabId, options) {
  // Inject selection script
  await chrome.scripting.executeScript({
    target: { tabId },
    files: ['selection.js']
  });

  // Wait for selection to complete
  return new Promise((resolve) => {
    chrome.runtime.onMessage.addListener(function listener(message) {
      if (message.type === 'selectionComplete') {
        chrome.runtime.onMessage.removeListener(listener);
        resolve(message.dataUrl);
      }
    });
  });
}

function downloadScreenshot(dataUrl) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const filename = `screenshot-${timestamp}.png`;
  
  chrome.downloads.download({
    url: dataUrl,
    filename: filename,
    saveAs: true
  });
} 