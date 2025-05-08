document.getElementById("sendButton").addEventListener("click", async function() {
    const message = document.getElementById("userMessage").value;
    const responseText = document.getElementById("responseText");

    if (!message) {
        alert("Please enter a message.");
        return;
    }

    try {
        const response = await fetch(`${CONFIG.API_BASE_URL}/chat`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: message }),
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.statusText}`);
        }

        const data = await response.json();
        responseText.textContent = data.response;
    } catch (error) {
        console.error("Error:", error);
        responseText.textContent = `Error: ${error.message}`;
    }
});
