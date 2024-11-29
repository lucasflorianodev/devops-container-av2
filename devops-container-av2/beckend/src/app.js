const express = require("express");
const app = express();

const PORT = 3000;

// Rota simples
app.get("/", (req, res) => {
  res.send("Hello from the backend!");
});

// Inicia o servidor
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});