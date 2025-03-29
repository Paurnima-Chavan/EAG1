// Create selection overlay
const overlay = document.createElement('div');
overlay.style.cssText = `
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 999999;
  cursor: crosshair;
`;

// Create selection box
const selectionBox = document.createElement('div');
selectionBox.style.cssText = `
  position: fixed;
  border: 2px solid #2196F3;
  background: rgba(33, 150, 243, 0.1);
  z-index: 1000000;
  display: none;
`;

document.body.appendChild(overlay);
document.body.appendChild(selectionBox);

let startX, startY, isSelecting = false;

// Mouse event handlers
overlay.addEventListener('mousedown', startSelection);
overlay.addEventListener('mousemove', updateSelection);
overlay.addEventListener('mouseup', endSelection);

function startSelection(e) {
  isSelecting = true;
  startX = e.clientX;
  startY = e.clientY;
  selectionBox.style.display = 'block';
  selectionBox.style.left = startX + 'px';
  selectionBox.style.top = startY + 'px';
}

function updateSelection(e) {
  if (!isSelecting) return;
  
  const currentX = e.clientX;
  const currentY = e.clientY;
  
  const left = Math.min(startX, currentX);
  const top = Math.min(startY, currentY);
  const width = Math.abs(currentX - startX);
  const height = Math.abs(currentY - startY);
  
  selectionBox.style.left = left + 'px';
  selectionBox.style.top = top + 'px';
  selectionBox.style.width = width + 'px';
  selectionBox.style.height = height + 'px';
}

async function endSelection(e) {
  if (!isSelecting) return;
  isSelecting = false;
  
  const rect = selectionBox.getBoundingClientRect();
  
  // Clean up
  overlay.remove();
  selectionBox.remove();
  
  // Capture the selected area
  try {
    const dataUrl = await chrome.runtime.sendMessage({
      type: 'captureArea',
      area: {
        x: rect.left,
        y: rect.top,
        width: rect.width,
        height: rect.height
      }
    });
    
    chrome.runtime.sendMessage({
      type: 'selectionComplete',
      dataUrl: dataUrl
    });
  } catch (error) {
    console.error('Failed to capture selected area:', error);
  }
} 