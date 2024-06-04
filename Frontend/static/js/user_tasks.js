document.addEventListener('DOMContentLoaded', () => {
	const new_task_form = document.querySelector('.new_task_form');
	const userId = new_task_form.dataset.userid;
	const accessToken = localStorage.getItem('accessToken');
	const tasksList = document.querySelector('.tasks-list');
    let editMode = false;
	let editTaskId = null;


	new_task_form.addEventListener('submit', async (event) => {
        event.preventDefault();

        const title = document.getElementById('task_title').value;
        const due_date = document.getElementById('task_due_date').value;
		const description = document.getElementById('task_description').value;

        let url = `http://127.0.0.1:5000/api/users/${userId}/tasks`;
        let method = 'POST';

        if (editMode) {
            url = `http://127.0.0.1:5000/api/users/${userId}/tasks/${editTaskId}`;
            method = 'PATCH';
        }

        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
				'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify({ title, due_date, description})
        });

        if (response.ok) {
			location.reload();
        } else {
            alert('Failed to create task. Please try again.');
        }
    });

	tasksList.addEventListener('click', async (event) => {
		if (event.target.classList.contains('delete-btn')) {
			const taskItem = event.target.closest('.task-item');
			const taskId = taskItem.dataset.taskId;

			const response = await fetch(`http://127.0.0.1:5000/api/users/${userId}/tasks/${taskId}`, {
				method: 'DELETE',
				headers: {
					'Authorization': `Bearer ${accessToken}`
				}
			});

			if (response.ok) {
				taskItem.remove();
			} else {
				alert('Failed to delete task. Please try again');
			}
		} else if (event.target.classList.contains('complete-btn')) {
            const taskItem = event.target.closest('.task-item');
            const taskId = taskItem.dataset.taskId;

            const response = await fetch(`http://127.0.0.1:5000/api/users/${userId}/tasks/${taskId}`, {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${accessToken}`
                },
                body: JSON.stringify({ completed: true })
            });

            if (response.ok) {
                taskItem.classList.add('completed');
				event.target.innerText = 'Completed';
            } else {
                alert('Failed to mark task as completed. Please try again.');
            }
		} else if (event.target.classList.contains('edit-btn')) {
            const taskItem = event.target.closest('.task-item');
            const taskId = taskItem.dataset.taskId;
            const title = taskItem.querySelector('.task-title').innerText;
            const due_date = taskItem.querySelector('.task-due-date').innerText;
            const description = taskItem.querySelector('.task-desc').innerText;

            console.log(`Title: ${title}, Due Date: ${due_date}, Description: ${description}`);

            document.getElementById('task_title').value = title;
            document.getElementById('task_due_date').value = due_date;
            document.getElementById('task_description').value = description;

            editMode = true;
            editTaskId = taskId;

            taskItem.remove();
        }
	});
});
