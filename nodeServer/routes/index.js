var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/screenshot', function(req, res, next) {
  var PythonShell = require('python-shell');

  PythonShell.run('/public/pythonscripts/screenshot.py', function (err,result) {
    if (err) throw err;
    console.log(result);
    res.render('screenshots',{res:result});
  });

//   var screenshot = require('desktop-screenshot');
//
// screenshot("/public/images/screenshot.png", function(error, complete) {
//     if(error)
//         console.log("Screenshot failed", error);
//     else
//         console.log("Screenshot succeeded");
// });
});

module.exports = router;
