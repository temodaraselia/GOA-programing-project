function playSound(event) {
    var audio = document.getElementById('sound');
    var targetUrl = event.currentTarget.closest('a').href;

    event.preventDefault();
    audio.currentTime = 0;
    audio.play();


    setTimeout(function() {
        window.location.href = targetUrl;
    }, 300); 
}