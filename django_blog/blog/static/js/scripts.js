// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.querySelector("form");

    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            // Example: Add basic validation before submitting
            const emailInput = loginForm.querySelector('input[type="email"]');
            const passwordInput = loginForm.querySelector('input[type="password"]');

            if (!emailInput.value || !passwordInput.value) {
                alert("Please fill in all fields.");
                event.preventDefault(); // Prevent form submission
            }
        });
    }
});
