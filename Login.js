//jshint esversion: 6

const express = require("express");
const bodyParser = require("body-parser");
const XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var jsdom = require("jsdom");
const AmazonCognitoIdentity = require('amazon-cognito-identity-js');
const CognitoUserPool = AmazonCognitoIdentity.CognitoUserPool;
const AWS = require('aws-sdk');
const request = require('request');
const jwkToPem = require ('jwk-to-pem');
const jwt = require('jsonwebtoken');
global.fetch = require('node-fetch');
const { JSDOM } = jsdom;
const { window } = new JSDOM();
const { document } = (new JSDOM('')).window;
global.document = document;

const poolData = {
  UserPoolId : "ap-southeast-1_npYY55FZJ",
  ClientId : "5ng046js96l2gcqefbiahjupet"
};
const pool_region = 'ap-southeast-1';
const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

function RegisterUser(userEmail, userPassword){
  var attributeList = [];
  attributeList.push(new AmazonCognitoIdentity.CognitoUserAttribute({Name:"email",Value:userEmail}));
  userPool.signUp(userEmail, userPassword, attributeList, null, function(err, result){
      if (err) {
          console.log(err);
          return;
      }
      cognitoUser = result.user;
      console.log('user name is ' + cognitoUser.getUsername());
  }); 
}

function Login(userEmail, userPassword) {
  var authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails({
      Username : userEmail,
      Password : userPassword,
  });

  var userData = {
      Username : userEmail,
      Pool : userPool
  };
  var cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);

  cognitoUser.authenticateUser(authenticationDetails, {
      onSuccess: function (result) {
          console.log('access token + ' + result.getAccessToken().getJwtToken());
          console.log('id token + ' + result.getIdToken().getJwtToken());
          console.log('refresh token + ' + result.getRefreshToken().getToken());
      },
      onFailure: function(err) {
          console.log(err);
      },

  });
}

var $ = require('jquery')(window);

const app = express();
app.use(bodyParser.json()); // to support JSON bodie
app.use(bodyParser.urlencoded({extended: true}));

app.use(express.static("public"));

app.get("/", function(req, res){
  res.sendFile(__dirname + "/index.html");
});

app.post("/", function(req, res){ // sign in
  var uEmail = req.body.uEmail;
  var uPassword = req.body.uPassword;
  Login(uEmail, uPassword);
  console.log(uEmail);
  console.log(uPassword);
});

app.post("/a", function(req, res){ //register
  var mail = req.body.mail;
  var pas = req.body.psw;
  RegisterUser(mail, pas);
});

app.listen(3000, function() {
  console.log("Server is running on port 3000");
});
