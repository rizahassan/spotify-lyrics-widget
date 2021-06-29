function changeText() {
  const { PythonShell } = require("python-shell");

  let pyshell = new PythonShell('./backend/script.py');

  pyshell.on('message',function(message){
      console.log(message);
      document.getElementById("text").innerHTML = message;
  })

  pyshell.end(function(err){
      if(err){
          throw err;
      };
      console.log('finished');
  });
}
