
document.getElementById("startButton").addEventListener("click", function() {
    const video = document.getElementById("video");
    const alertBox = document.getElementById("alertBox");

    // Access webcam
    navigator.mediaDevices.getUserMedia({ video: true })
        .then(function(stream) {
            video.srcObject = stream;
        })
        .catch(function(err) {
            console.error("Error accessing webcam: " + err);
        });

    // Handle motion detection alerts via WebSocket
    const socket = new WebSocket("ws://127.0.0.1:5000");
    
    socket.onmessage = function(event) {
        if (event.data === "motion detected") {
            alertBox.style.display = "block"; // Show alert box
            setTimeout(function() {
                alertBox.style.display = "none"; // Hide alert box after 3 seconds
            }, 3000);
        }
    };

    // Send sensitivity value to the server on slider change
    const sensitivitySlider = document.getElementById('sensitivity');
    sensitivitySlider.addEventListener('input', function() {
        const sensitivityValue = sensitivitySlider.value;
        socket.send(JSON.stringify({ type: 'set_sensitivity', value: sensitivityValue }));
        document.getElementById('sensitivityValue').textContent = sensitivityValue;
    });
});
