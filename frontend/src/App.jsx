import { useState } from "react";

function App() {
 
  const [rainfall, setRainfall] = useState("");
  const [slope, setSlope] = useState("");
  const [soil, setSoil] = useState("clay");
  const [result, setResult] = useState("");

  const predict = async () => {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        rainfall: Number(rainfall),
        slope: Number(slope),
        soil_type: soil,
      }),
    });

    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1> Landslide Risk Prediction System </h1>

      <label>Rainfall</label><br />
      <input
        value={rainfall}
        onChange={(e) => setRainfall(e.target.value)}
      /><br /><br />

      <label>Slope</label><br />
      <input
        value={slope}
        onChange={(e) => setSlope(e.target.value)}
      /><br /><br />

      <label>Soil Type</label><br />
      <select value={soil} onChange={(e) => setSoil(e.target.value)}>
        <option value="clay">Clay</option>
        <option value="sand">Sand</option>
        <option value="loam">Silt</option>
      </select><br /><br />

      <button style={{ marginBottom: "20px", fontSize: "16px" }} onClick={predict}>Predict</button>

      <h2>{result}</h2>
    </div>
  );
}

export default App;