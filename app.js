"use strict"
var express = require("express");
var bodyParser = require("body-parser");
var app = express();
var mutation_routes = require("./routes/mutation");
app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());
app.use("/api", mutation_routes);
module.exports = app;