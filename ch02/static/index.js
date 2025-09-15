const count = document.getElementById("count");
const num = document.getElementById("num")
const submit = document.getElementById("submit");

let number = 0;
count.addEventListener('click', () => {
    number++;
    num.innerHTML = number;
});

submit.addEventListener('click', async () => {
    let res = await fetch("/submit", {
        method: "POST",
        headers: {"Content-Type":"application/json"},
        body: JSON.stringify({ value: number })
    });
    number = 0;
    num.innerHTML = number;
});