//시계 구현
setInterval(myWatch, 1000)

function myWatch(){
    var date = new Date();
    var now = date.toLocaleTimeString();
    document.getElementById('demo').innerHTML = now;
}
