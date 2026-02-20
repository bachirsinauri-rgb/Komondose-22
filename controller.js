const API_URL = "http://localhost:8080/ask?q=";

async function sendToBrain(query) {
    try {
        const response = await fetch(API_URL + encodeURIComponent(query));
        const data = await response.json();
        return data.reply;
    } catch (error) {
        return "فشل الاتصال بعقل سندي في Termux.";
    }
}
