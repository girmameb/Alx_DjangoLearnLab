// blog/static/js/scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.querySelector("form");

    if (loginForm) {
        loginForm.addEventListener("submit", function(event) {
            const usernameInput = loginForm.querySelector('input[name="username"]');
            const passwordInput = loginForm.querySelector('input[name="password"]');

            if (!usernameInput.value || !passwordInput.value) {
                alert("Please fill in all fields.");
                event.preventDefault(); // Prevent form submission
            }
        });
    }
});
