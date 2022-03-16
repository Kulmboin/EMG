const pythonShell = require('python-shell');

var options = {
  mode: 'text',
  pythonPath: '',
  pythonOptions: ['-u'],
  scriptPath: '',
  args: [arg1,arg2]
};

pythonShell.PythonShell.run('test2.py', options, function (err, results) {
      if (err) console.log(err);
      else console.log(results);
});