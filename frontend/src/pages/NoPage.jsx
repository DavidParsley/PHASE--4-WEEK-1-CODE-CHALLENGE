import React from "react";


export default function NoPage() {
  return (
    <div className="no-page-container">
      <div className="no-page-content">
        <h1>404</h1>
        <p>The page you are trying to access doesn't exist.</p>
        <a href={"/"} className="back-home">Go Back to Home</a>
      </div>
    </div>
  );
}
