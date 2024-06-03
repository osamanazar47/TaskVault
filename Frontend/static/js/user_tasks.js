document.addEventListener('DOMContentLoaded', () => {
	const new_task_form = document.querySelector('.new_task_form');

	new_task_form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const title = document.getElementById('task_title').value;
        const due_date = document.getElementById('task_due_date').value;
		const description = document.getElementById('description').value;
		const urlParams = new URLSearchParams(window.location.search);
		const userId = urlParams.get('user_id');
		const accessToken = localStorage.getItem('accessToken')

        const response = await fetch(`http://127.0.0.1:5000/api/users/${userId}/tasks`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
				'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify({ title: title, due_date: due_date, description: description })
        });

        if (response.ok) {
			alert('Task created successfuly')
        } else {
            alert('Failed to create task. Please try again.');
        }
    });

});