import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/tokens.generated.css";
import "./styles/base.css";
import "./styles/atoms.css";
import "./styles/molecules.css";
import "./styles/organisms.css";
import "./styles/pages.css";
import "./styles/panel.css";

ReactDOM.createRoot(document.getElementById("root")!).render(<React.StrictMode><App /></React.StrictMode>);
