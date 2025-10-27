const now = document.getElementById("now");
const record = document.getElementById("record");
const table = document.getElementById("table");

now.addEventListener('click', () => {
    console.log("done");
    $.ajax({
    type: 'GET',
    url: '/api/now',
    contentType: 'application/json'
  }).done((result) => {
    console.log("done");
    console.log(result);

    const div = document.createElement("div");
    div.className = "row";

    const no = document.createElement("p");
    const time = document.createElement("p");
    const temperature = document.createElement("p");
    const humidity = document.createElement("p");
    
    no.textContent = "now";
    time.textContent = result.create_at;
    temperature.textContent = result.temperature;
    humidity.textContent = result.humidity;
    
    div.appendChild(no);
    div.appendChild(time);
    div.appendChild(temperature);
    div.appendChild(humidity);

    table.appendChild(div);
  }).fail((result) => {
    console.log("fail");
    console.log(result);
  });
});
