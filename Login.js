//jshint esversion: 6

const express = require("express");
const bodyParser = require("body-parser");
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var jsdom = require("jsdom");
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;

var $ = require('jquery')(window);

const app = express();
app.use(bodyParser.json()); // to support JSON bodie
app.use(bodyParser.urlencoded({extended: true}));

app.use(express.static("public"));

app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html");
});

app.post("/", function(req, res){
  var uEmail = req.body.uEmail;
  var uPassword = req.body.uPassword;
  console.log(uEmail+uPassword);
});

app.post("/a", function(req, res){
  var mail = req.body.mail;
  var pas = req.body.psw;
  var add1 = req.body.address1;
  var add2 = req.body.address2;
  var postal = req.body.postal;
  console.log(mail+pas+add1+add2+postal);
});

app.listen(3000, function() {
  console.log("Server is running on port 3000");
});
