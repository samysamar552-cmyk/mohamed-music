let playing = false;

function playSong(name) {
    document.getElementById("currentSong").innerText = name;
    playing = true;

    document.querySelector(".play-button").innerText = "⏸";
}

function togglePlay() {
    if (
        !document.getElementById("currentSong").innerText ||
        document.getElementById("currentSong").innerText === "لم يتم اختيار أغنية"
    ) {
        return;
    }

    playing = !playing;

    document.querySelector(".play-button").innerText =
        playing ? "⏸" : "▶";
}