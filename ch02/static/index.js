const count = document.getElementById("count");
const num = document.getElementById("num")
const submit = document.getElementById("submit");

let number = 0;
count.addEventListener('click', () => {
    number++;
    num.innerHTML = number;
});

submit.addEventListener('click', () => {
    location.href = `http://127.0.0.1:5001/submit?num=${number}`;
});