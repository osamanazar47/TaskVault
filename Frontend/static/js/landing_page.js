document.addEventListener('DOMContentLoaded', () => {
    const signupToggle = document.getElementById('signup-toggle');
    const loginToggle = document.getElementById('login-toggle');
    const signupForm = document.getElementById('signupForm');
    const loginForm = document.getElementById('loginForm');

    signupToggle.addEventListener('click', () => {
        signupToggle.classList.add('active');
        loginToggle.classList.remove('active');
        signupForm.classList.add('active');
        loginForm.classList.remove('active');
    });

    loginToggle.addEventListener('click', () => {
        loginToggle.classList.add('active');
        signupToggle.classList.remove('active');
        loginForm.classList.add('active');
        signupForm.classList.remove('active');
    });

    signupForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const username = document.getElementById('signupUsername').value;
        const password = document.getElementById('signupPassword').value;

        const response = await fetch('http://127.0.0.1:5000/api/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: username, password: password })
        });

        if (response.ok) {
            signupForm.reset();
        } else {
            alert('Signup failed!');
        }
    });

    loginForm.addEventListener('submit', async (event) => {
        event.preventDefault();

        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        const response = await fetch('http://127.0.0.1:5000/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: username, password: password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('accessToken', data.access_token);
            window.location.href = `http://127.0.0.1:5000/tasks/${data.user_id}`;
            loginForm.reset();
        } else {
            alert('Login failed!');
        }
    });

    gsap.from(".header", { duration: 1, y: -100, opacity: 0 });
    gsap.from(".intro-text", { duration: 1, x: -100, opacity: 0, delay: 0.5 });
    gsap.from(".features-section", { duration: 1, y: 100, opacity: 0, delay: 1 });
    gsap.from(".form-container", { duration: 1, x: 100, opacity: 0, delay: 1.5 });
    gsap.from(".reviews", { duration: 1, y: 100, opacity: 0, delay: 2 });
});
