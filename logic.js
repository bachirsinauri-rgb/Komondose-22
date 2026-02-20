const CONFIG = {
    SERVER_URL: "http://localhost:8080",
    VERSION: "V24.0"
};
async function triggerAction(actionName) {
    const term = document.getElementById('terminal-box');
    term.innerHTML += `<div style="color:red">⚠️ جاري تنفيذ: ${actionName}...</div>`;
    const response = await fetch(`${CONFIG.SERVER_URL}/ask?q=${encodeURIComponent(actionName)}`);
    const data = await response.json();
    term.innerHTML += `<div style="color:lime">> رد سندي: ${data.reply}</div>`;
}
