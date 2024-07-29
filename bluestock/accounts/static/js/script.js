
document.addEventListener("DOMContentLoaded", function() {
   
    const togglePassword1 = document.querySelector("#togglePassword1");
    const togglePassword2 = document.querySelector("#togglePassword2");
    const password1 = document.querySelector("#password");
    const password2 = document.querySelector("#password2");
   

    let timeoutId1; // to store the timeout ID for password1
    let timeoutId2; // to store the timeout ID for password2

    // Function to handle the toggle logic
    function togglePasswordVisibility(toggleButton, passwordField, timeoutId) {
        if (!toggleButton || !passwordField) {
            console.error("Element not found: ", toggleButton, passwordField);
            return;
        }

        clearTimeout(timeoutId); // Clear any existing timeout

        // Toggle the type attribute
        const type = passwordField.getAttribute("type") === "password" ? "text" : "password";
        passwordField.setAttribute("type", type);

        // Toggle the eye icon
        toggleButton.classList.toggle("fa-eye-slash");
        toggleButton.classList.toggle("fa-eye");

        // If the type is now text, set a timeout to change it back to password
        if (type === "text") {
            timeoutId = setTimeout(() => {
                passwordField.setAttribute("type", "password");
                // Reset the eye icon
                toggleButton.classList.toggle("fa-eye-slash");
                toggleButton.classList.toggle("fa-eye");
            }, 800); // 800 milliseconds
        }
        return timeoutId; // Return the new timeout ID
    }

    // Add event listener for the first toggle button
    if (togglePassword1 && password1) {
        togglePassword1.addEventListener("click", function () {
            timeoutId1 = togglePasswordVisibility(this, password1, timeoutId1);
        });
    }

    // Add event listener for the second toggle button
    if (togglePassword2 && password2) {
        togglePassword2.addEventListener("click", function () {
            timeoutId2 = togglePasswordVisibility(this, password2, timeoutId2);
        });
    }

})


