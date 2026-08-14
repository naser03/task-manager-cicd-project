const form = document.getElementById("task-form");
const input = document.getElementById("task-input");
const taskList = document.getElementById("task-list");
const statusText = document.getElementById("status");
const API_BASE_URL = "http://localhost:5000";

const API_BASE_URL =
    window.location.port === "5500"
        ? "http://localhost:5000"
        : "";

async function api(path, options = {}) {
    const response = await fetch(`${API_BASE_URL}${path}`, {
        headers: {
            "Content-Type": "application/json",
            ...(options.headers || {})
        },
        ...options
    });

    if (!response.ok) {
        const error = await response.json().catch(() => ({}));
        throw new Error(error.error || "Request failed");
    }

    return response.json();
}

async function checkHealth() {
    try {
        const result = await api("/api/health");
        // statusText.textContent = `Backend: ${result.status}`;
        statusText.className = "status online";
    } catch (error) {
        statusText.textContent = "Backend unavailable";
        statusText.className = "status offline";
    }
}

async function loadTasks() {
    try {
        const tasks = await api("/api/tasks");

        if (tasks.length === 0) {
            taskList.innerHTML = '<p class="empty">No tasks yet.</p>';
            return;
        }

        taskList.innerHTML = tasks.map(task => `
            <article class="task ${task.completed ? "completed" : ""}">
                <button
                    class="check"
                    onclick="toggleTask(${task.id})"
                    aria-label="Toggle task"
                >
                    ${task.completed ? "✓" : ""}
                </button>

                <span>${escapeHtml(task.title)}</span>

                <button
                    class="delete"
                    onclick="deleteTask(${task.id})"
                >
                    Delete
                </button>
            </article>
        `).join("");
    } catch (error) {
        taskList.innerHTML = `<p class="error">${error.message}</p>`;
    }
}

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const title = input.value.trim();

    if (!title) {
        return;
    }

    try {
        await api("/api/tasks", {
            method: "POST",
            body: JSON.stringify({ title })
        });

        input.value = "";
        await loadTasks();
    } catch (error) {
        alert(error.message);
    }
});

async function toggleTask(id) {
    await api(`/api/tasks/${id}`, {
        method: "PATCH"
    });

    await loadTasks();
}

async function deleteTask(id) {
    await api(`/api/tasks/${id}`, {
        method: "DELETE"
    });

    await loadTasks();
}

function escapeHtml(value) {
    const div = document.createElement("div");
    div.textContent = value;
    return div.innerHTML;
}

checkHealth();
loadTasks();
