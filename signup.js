function submitForm() {
  // Get form data
  const firstname = document.getElementById("firstname").value;
  const lastname = document.getElementById("lastname").value;
  const email = document.getElementById("email").value;
  const company = document.getElementById("company").value;

  // Data to send in the AJAX request
  const data = { firstname, lastname, email, company };

  // AJAX request to send data to FastAPI
  fetch("http://127.0.0.1:8000/signup", {
      method: "POST",
      headers: {
          "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
  })
  .then(response => response.json())
  .then(data => {
      alert(data.message);  // Show success message
  })
  .catch((error) => {
      console.error("Error:", error);
      alert("There was an error submitting the form.");
  });
}
