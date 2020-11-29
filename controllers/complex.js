"use strict"
var Complex = require("../models/complex");
var path = require("path");
var fs = require("fs");
var controller = {
    getComplex: (req, res) =>{
        //Devuelve un listado de mutaciones que se han encontrado junto a la entregada por parámetro. 
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        console.log(mutationName);
        //Valida si ingresó nombre de la mutación correctamente. 
        if(!mutationName || mutationName == undefined){
            if(!mutationName){
                console.log("getCaseComplex Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Complex.find({"Mutations": mutationName}).exec((err, complex)=>{
            //Valida si existe la mutación en la colección complex. 
            if(err){
                console.log("getCaseComplex No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getCouples Success");
            //Retorna la mutación compleja. 
            return res.status(200).send({
                complex
            })
        });
    },
    getCouples: (req, res) =>{
        //Devuelve el caso complejo en el que se encuentra una mutación del grupo entregada por parámetro. 
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        console.log(mutationName);
        //Valida si ingresó nombre de la mutación correctamente. 
        if(!mutationName || mutationName == undefined){
            if(!mutationName){
                console.log("getCaseComplex Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Complex.find({"Mutations": mutationName}, {"Mutations": 1}).distinct("Mutations").exec((err, couples)=>{
            //Valida si existe la mutación en la colección complex. 
            if(err){
                console.log("getCaseComplex No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getCouples Success");
            //Retorna la mutación compleja. 
            return res.status(200).send({
                couples
            })
        });
    },
    getCaseCouples: (req, res) =>{
        //Devuelve el caso en el que se encuentra un grupo de mutaciones (grupo especificado).
    },
};
module.exports = controller;