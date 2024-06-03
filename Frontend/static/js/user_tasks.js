document.addEventListener('DOMContentLoaded', () => {
	const new_task_form = document.querySelector('.new_task_form');

	new_task_form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const title = document.getElementById('task_title').value;
        const due_date = document.getElementById('task_due_date').value;
		const description = document.getElementById('description').value;
		const userId = window.location.pathname.split('/').pop();
		const accessToken = localStorage.getItem('accessToken')

		console.log("Form data:", { title, due_date, description });
        console.log("User ID:", userId);
        console.log("Access Token:", accessToken);

        const response = await fetch(`http://127.0.0.1:5000/api/users/${userId}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
				'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify({ title, due_date, description})
        });

        if (response.ok) {
			alert('Task created successfuly')
        } else {
            alert('Failed to create task. Please try again.');
        }
    });

});