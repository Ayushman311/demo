function togglePasswordVisibility() {
    var passwordInput = document.getElementById("password");
    var eyeIcon = document.querySelector(".toggle-password");
    
    if (passwordInput.type === "password") {
      passwordInput.type = "text";
      eyeIcon.style.backgroundImage = "url('eye-open-icon.png')"; /* Change to open eye icon */
    } else {
      passwordInput.type = "password";
      eyeIcon.style.backgroundImage = "url('eye-icon.png')"; /* Change to closed eye icon */
    }
  }
  