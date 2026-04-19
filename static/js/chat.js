const messages = document.getElementById('messages');
const input = document.getElementById('question');
const sendBtn = document.getElementById('send-btn');

function appendMessage(text, role) {
    const div = document.createElement('div');
    div.classList.add('message', role);
    div.textContent = text;
    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}

sendBtn.addEventListener('click', async () => {
    const question = input.value.trim();
    if (!question) return;

    appendMessage(question, 'user');
    input.value = '';

    const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question })
    });

    const data = await res.json();
    appendMessage(data.answer || 'Something went wrong.', 'bot');
});

input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') sendBtn.click();
});
