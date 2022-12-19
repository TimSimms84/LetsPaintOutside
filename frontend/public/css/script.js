let paintingAPI = {
  apiKey: "563492ad6f91700001000001332003b90d6b4d7789b263cd42f38d58",
  fetchData: function (subject) {
    fetch("http://localhost:8000/api/subject/" + subject)
      .then((response) => response.json())
      .then((data) => {
        console.log(data[0]);
        let randomVideo = this.randomNumber(0, data.length - 1);
        // console.log(randomVideo);
        const youtube_src = data[randomVideo].youtube_src;
        console.log(youtube_src);
        this.displayData(subject)
        this.changeVideo(youtube_src)
      });
  },
  displayData: function (data) {
    document.body.style.backgroundImage = "url('https://source.unsplash.com/1600x900/?" + data  + "')";
  },
  changeVideo: function (data) {
    console.log(data)
    document.querySelector(".video").src = data;
  },
  randomNumber: function (min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
  },
  search: function () {
    this.fetchData(document.querySelector(".search-bar").value);
  }
}

document.querySelector(".search button")
.addEventListener("click", function () {
  paintingAPI.search();
});

document.querySelector(".search-bar")
.addEventListener("keyup", function (event) {
  if (event.key === "Enter") {
    paintingAPI.search();
  }
});
