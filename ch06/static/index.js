const now = document.getElementById("now");
const record = document.getElementById("record");
const table = document.getElementById("table");

now.addEventListener('click', () => {
  $.ajax({
    type: 'GET',
    url: '/api/now',
    contentType: 'application/json'
  }).done((result) => {
    console.log(result);

    const div = document.createElement("div");
    div.className = "row";

    const no = document.createElement("p");
    const time = document.createElement("p");
    const temperature = document.createElement("p");
    const humidity = document.createElement("p");
    no.textContent = "now";
    time.textContent = "now";
    temperature.textContent = result.temp;
    humidity.textContent = result.hum;
    
    div.appendChild(no);
    div.appendChild(time);
    div.appendChild(temperature);
    div.appendChild(humidity);
  }).fail((result) => {
    console.log(result);
  });
});