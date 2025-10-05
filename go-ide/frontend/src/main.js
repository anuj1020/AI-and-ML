// File: go-ide/frontend/src/main.js
import './style.css';
import * as backend from '../wailsjs/go/main/App.js';

// Set up the basic HTML structure
document.querySelector('#app').innerHTML = `
    <div class="app-container">
        <div id="sidebar" class="sidebar">
            <div class="sidebar-header">
                <h3>Project Explorer</h3>
                <button id="btnOpenProject">Open Folder</button>
            </div>
            <div id="file-tree" class="file-tree"></div>
        </div>
        <div class="main-content">
            <div id="editor-container" class="editor-container">
                <div id="welcome-screen">
                    <h1>Welcome to GoCode IDE</h1>
                    <p>Click "Open Folder" to begin.</p>
                </div>
            </div>
             <div id="status-bar" class="status-bar">
                <span id="status-message">Ready</span>
            </div>
        </div>
    </div>
`;

// --- Elements ---
const fileTreeEl = document.getElementById('file-tree');
const editorEl = document.getElementById('editor');
const welcomeScreenEl = document.getElementById('welcome-screen');
const statusMessageEl = document.getElementById('status-message');
const openProjectBtn = document.getElementById('btnOpenProject');

let currentFilePath = null;

// --- Event Listeners ---
openProjectBtn.addEventListener('click', () => {
    backend.OpenProject().then(project => {
        renderFileTree(project.fileTree, fileTreeEl);
        updateStatus(`Opened project: ${project.name}`);
    }).catch(err => {
        console.error(err);
        updateStatus(`Error: ${err}`);
    });
});

// --- Functions ---

function renderFileTree(nodes, container) {
    container.innerHTML = ''; // Clear existing tree
    nodes.forEach(node => {
        const item = document.createElement('div');
        item.textContent = node.name;
        item.dataset.path = node.path;

        if (node.isDir) {
            item.classList.add('dir-item');
            // Recursively render children if they exist
            if (node.children && node.children.length > 0) {
                const childrenContainer = document.createElement('div');
                childrenContainer.style.paddingLeft = '15px';
                renderFileTree(node.children, childrenContainer);
                item.appendChild(childrenContainer);
            }
        } else {
            item.classList.add('file-item');
            item.addEventListener('click', () => onFileClick(node.path));
        }
        container.appendChild(item);
    });
}

function onFileClick(path) {
    updateStatus(`Opening ${path}...`);
    backend.ReadFileContents(path).then(content => {
        editorEl.value = content;
        currentFilePath = path;
        welcomeScreenEl.style.display = 'none';
        editorEl.style.display = 'block';
        updateStatus(`Editing ${path}`);
    }).catch(err => {
        console.error("Failed to read file:", err);
        updateStatus(`Error opening file: ${err}`);
    });
}

function updateStatus(message) {
    statusMessageEl.textContent = message;
}

// Global key listeners
window.addEventListener('keydown', (e) => {
    // Save on Ctrl+S or Cmd+S
    if ((e.ctrlKey || e.metaKey) && e.key === 's') {
        e.preventDefault();
        if (currentFilePath) {
            updateStatus(`Saving...`);
            backend.SaveFileContents(currentFilePath, editorEl.value).then(() => {
                updateStatus(`Saved ${currentFilePath}`);
            }).catch(err => {
                updateStatus(`Error saving: ${err}`);
            });
        }
    }
});


// --- Initial State ---
function main() {
    editorEl.style.display = 'none';
    updateStatus('Ready. Open a folder to begin.');
}

// Wails exposes a 'Ready' function that we can use for setup.
window.wails.events.on("wails:ready", main);