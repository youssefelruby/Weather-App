document.getElementById("getWeatherBtn").addEventListener("click", async () => {
    const zipCode = document.getElementById("zipInput").value;
    const resultElement = document.getElementById("weatherResult");
  
    if (!zipCode) {
      resultElement.innerText = "Please enter a valid ZIP code!";
      return;
    }
  
    try {
      // Make a request to our own microservice (running on localhost:3000 for example)
      const response = await fetch(`http://localhost:3000/weather?zip=${zipCode}`);
  
      if (!response.ok) {
        // If the response is not OK (e.g. 404, 500, etc.)
        throw new Error("Server response wasn't OK");
      }
  
      const data = await response.json();
  
      // Display the weather info
      resultElement.innerText = `Current temperature: ${data.temperature}°F and weather: ${data.condition}`;
    } catch (error) {
      console.error("Error fetching weather data:", error);
      resultElement.innerText = "Error fetching weather data. Please try again later.";
    }
  });
  