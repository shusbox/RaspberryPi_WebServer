const now = document.getElementById("now");
const record = document.getElementById("record");

now.addEventListener('click', () => {
  $.ajax({
    type: 'GET',
    url: '/choiruru',
    contentType: 'application/json'
  }).done(() => {
    console.log(result);
  }).fail(() => {
    console.log(result);
  });
});