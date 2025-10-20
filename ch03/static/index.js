const onRed = document.getElementById("onRedBtn");
const offRed = document.getElementById("offRedBtn");
const onYellow = document.getElementById("onYellowBtn");
const offYellow = document.getElementById("offYellowBtn");
const onGreen = document.getElementById("onGreenBtn");
const offGreen = document.getElementById("offGreenBtn");
const onAll = document.getElementById("onAllBtn");
const offAll = document.getElementById("offAllBtn");

onRed.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/redOn';
});
offRed.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/redOff';
});

onYellow.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/yellowOn';
});
offYellow.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/yellowOff';
});

onGreen.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/greenOn';
});
offGreen.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/greenOff';
});

onAll.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/on';
});
offAll.addEventListener('click', () => {
    location.href='http://10.150.2.125:5000/off';
});
