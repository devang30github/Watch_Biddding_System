// register.js

document.addEventListener('DOMContentLoaded', function() {
    var usernameField = document.getElementById('id_username');
    var passwordField = document.getElementById('id_password1');
    var passwordConfirmationField = document.getElementById('id_password2');
    var usernameValidationMessage = document.querySelector('.username-validation-message');
    var passwordValidationMessages = document.querySelectorAll('.password-validation-message');

    function validateUsername() {
        // Implement username validation logic here
        // Example: Check if username meets certain criteria
        if (usernameField.value.length < 3) {
            usernameValidationMessage.textContent = 'Username must be at least 3 characters long.';
        } else {
            usernameValidationMessage.textContent = ''; // Clear previous error messages
        }
    }

    function validatePasswords() {
        // Implement password validation logic here
        // Example: Check if passwords match
        if (passwordField.value !== passwordConfirmationField.value) {
            passwordValidationMessages.forEach(function(message) {
                message.textContent = 'Passwords do not match.';
            });
        } else {
            passwordValidationMessages.forEach(function(message) {
                message.textContent = ''; // Clear previous error messages
            });
        }
    }

    usernameField.addEventListener('input', validateUsername);
    passwordField.addEventListener('input', validatePasswords);
    passwordConfirmationField.addEventListener('input', validatePasswords);
});
