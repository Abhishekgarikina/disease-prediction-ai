// Update system status dynamically
const statusText = document.getElementById("statusText");

function updateStatus() {
    fetch('/health')
        .then(response => response.json())
        .then(data => {
            statusText.innerText = "System Status: " + data.status;
        })
        .catch(() => {
            statusText.innerText = "System Error";
        });
}

// Refresh status every 2 seconds
setInterval(updateStatus, 2000);

// Initial call
updateStatus();

console.log("Frontend loaded successfully");