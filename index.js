"use strict"
var mongoose = require("mongoose");
var app = require("./app");
var port = 3800;
mongoose.Promise = global.Promise;
mongoose.connect("mongodb://localhost:27017/VHL_Hunter", {useNewUrlParser:true})
.then(()=>{
    console.log("Conexión exitosa");
    app.listen(port, ()=>{
        console.log("Servidor corriendo");
    });
}).catch(err => console.log(err));