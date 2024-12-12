// Simple form validation for contact form
document.getElementById("contact-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form from submitting

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const message = document.getElementById("message").value;
    console.log("Welcome to Lets-dial!");

    if (name && email && message) {
        alert(`Thank you for reaching out, ${name}! We will get back to you shortly.`);
        // Reset form fields after submission
        document.getElementById("contact-form").reset();
    } else {
        alert("Please fill in all fields.");
    }
});
