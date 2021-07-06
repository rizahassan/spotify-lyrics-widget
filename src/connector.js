
function changeText() {
    // Display/Hide the get lyric button
    var lyricButton = document.getElementById("lyric-button");
    if (lyricButton.style.display === "none") {
        lyricButton.style.display = "block";
      } else {
        lyricButton.style.display = "none";
      }

  const { PythonShell } = require("python-shell");

  let artist = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    args: ["artist"],
  };

  let song = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    args: ["song"],
  };

  let lyric = {
    mode: "text",
    pythonOptions: ["-u"], // get print results in real-time
    args: ["lyric"],
  };

  let artistCommand = new PythonShell("./backend/script.py", artist);
  let songCommand = new PythonShell("./backend/script.py", song);
  let lyricCommand = new PythonShell("./backend/script.py", lyric);

  artistCommand.on("message", function (message) {
    console.log(message);
    document.getElementById("artist-name").innerHTML = message;
  });

  artistCommand.end(function (err) {
    if (err) {
      throw err;
    }
    console.log("Artist command finished");
  });

  songCommand.on("message", function (message) {
    console.log(message);
    document.getElementById("song-title").innerHTML = message;
  });

  songCommand.end(function (err) {
    if (err) {
      throw err;
    }
    console.log("Song command finished");
  });

  lyricCommand.on("message", function (message) {
    console.log(message);
    document.getElementById("lyrics").innerHTML = message;
  });

  lyricCommand.end(function (err) {
    if (err) {
      throw err;
    }
    console.log("Lyric command finished");
  });

  
}

// function authenticate(){
//     const { PythonShell } = require("python-shell");

//     let authenticate = {
//         mode: "text",
//         pythonOptions: ["-u"], // get print results in real-time
//         args: ["authenticate"],
//       };

//     let authenticateCommand = new PythonShell("./backend/script.py", authenticate);

//     authenticateCommand.on("message", function (message) {
//     console.log(message);
//     });

//     authenticateCommand.end(function (err) {
//     if (err) {
//         throw err;
//     }
//     console.log("Lyric command finished");
//     });
    

// }
