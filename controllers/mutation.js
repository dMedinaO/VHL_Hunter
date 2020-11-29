"use strict"
var Mutation = require("../models/mutation");
var path = require("path");
var fs = require("fs");
var controller = {
    //CONSULTAS
    getMutation: (req, res) => {
        //Método para obtener toda la información de la mutación especificada como parámetro (nombre). 
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación correctamente. 
        if(!mutationName || mutationName == undefined){
            if(!mutationName){
                console.log("getMutation Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({"Mutation": mutationName}).exec((err, mutation)=>{
            //Valida si existe la mutación en la colección. 
            if(err || mutation.length == 0){
                console.log("getMutation No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getMutacion Success");
            //Retorna la mutación. 
            return res.status(200).send({
                mutation
            })
        });
    },
    getCases: (req, res) =>{
        //Retorna los casos en los que se ha asociado la mutación ingresada
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación. 
        if(!mutationName || mutationName == undefined){
            if(!mutationName){
                console.log("getCases Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({"Mutation": mutationName}, {"Case": 1}).exec((err, cases)=>{
            //Valida si existe la mutación
            if(err || cases.length == 0){
                console.log("getCases No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getMutation Success");
            //Retorna la mutación.
            return res.status(200).send({
                cases
            })
        });
    },
    getEffects: (req, res) => {
        //Método para obtener un listado con los efectos de una determinada mutacion. 
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación correctamente. 
        if(!mutationName || mutationName == undefined){
            if(!mutationName){
                console.log("getEffects Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({"Mutation": mutationName}, {"Case.Disease.Effect": 1}).distinct("Case.Disease.Effect").exec((err, effects)=>{
            //Valida si existe la mutación
            if(err || effects.length == 0){
                console.log("getEffects No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getEffects Success");
            //Retorna la mutación. 
            return res.status(200).send({
                effects
            })
        });
    }, 
    getVHL: (req,res) => {
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación. 
        if(!mutationName || mutationName == undefined){
            if(!mutationName){
                console.log("getVHL Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({"Mutation": mutationName},{"Case.VHL_type": 1}).distinct("Case.VHL_type").exec((err, vhl)=>{
            //Valida si existe la mutación en la colección
            if(err || vhl.length == 0){
                console.log("getVHL No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getVHL Success");
            //Retorna la mutación. 
            return res.status(200).send({
                vhl
            })
        });
    },
    getMutationsbyEffect: (req, res) => {
        //Metodo para obtener las mutaciones que cumplen con un efecto.
        //Parámetros llegan por params. 
        var effect = req.params.effect;
        //Valida si ingresó el efecto. 
        if(!effect || effect == undefined){
            if(!effect){
                console.log("getMutationbyEffect Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({"Case.Disease": {"Effect": effect}}).exec((err, mutation)=>{
            //Valida si existe el efecto en la colección.
            if(err || mutation.length == 0){
                console.log("getMutationbyEffect No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getMutationbyEffect Success");
            //Retorna las mutaciones. 
            return res.status(200).send({
                mutation
            })
        });
    },
    getMutationsbyRisk: (req, res) => {
        //Método para obtener las mutaciones que cumplen con un riesgo clínico. 
        //Parámetros llegan por params. 
        var risk = req.params.risk;
        //Valida si ingresó el riesgo clínico para RCC. 
        if(!risk || risk == undefined){
            if(!risk){
                console.log("getMutationsbyRisk Error");
                return res.status(404).send({
                    message: "Risk isn't defined"
                });
            }
        }
        Mutation.find({"Risk": risk}).exec((err, mutation)=>{
            //Valida si existe la mutación
            if(err || mutation.length == 0){
                console.log("getMutationsbyRisk No data");
                return res.status(404).send({
                    message: "Risk don't exists"
                });
            }
            console.log("getMutationsbyRisk Success");
            //Retorna la mutación. 
            return res.status(200).send({
                mutation
            })
        });
    },
    getMutationsbyType: (req,res) => {
        //Método para obtener las mutaciones que cumplen con un tipo de mutacion. 
        //Parámetros llegan por params. 
        var mutationType = req.params.mutationType;
        //Valida si ingresó el tipo de la mutación.  
        if(!mutationType || mutationType == undefined){
            if(!mutationType){
                console.log("getMutationsbyType Error");
                return res.status(404).send({
                    message: "Type isn't defined"
                });
            }
        }
        Mutation.find({"Mutation_type": mutationType}).exec((err, mutations)=>{
            //Valida si existe la mutación
            if(err || mutations.length == 0){
                console.log("getMutationsbyType No data");
                return res.status(404).send({
                    message: "Type don't exists"
                });
            }
            console.log("getMutationsbyType Success");
            //Retorna la mutación. 
            return res.status(200).send({
                mutations
            })
        });
    },
    getMutationsbyVHL: (req, res) => {
        //Método para obtener las mutaciones que cumplen con un tipo de VHL. 
        //Parámetros llegan por params. 
        var vhlType = req.params.vhlType;
        //Valida si ingresó nombre. 
        if(!vhlType || vhlType == undefined){
            if(!vhlType){
                console.log("getMutationsbyVHL Error")
                return res.status(404).send({
                    message: "VHL type isn't defined"
                });
            }
        }
        Mutation.find({"Case.VHL_type": vhlType}).exec((err, mutations)=>{//Por ahí va
            //Valida si existe el tipo de VHL
            if(err || mutations.length == 0){
                console.log("getMutationsbyVHL No Data");
                return res.status(404).send({
                    message: "VHL don't exists"
                });
            }
            console.log("Success");
            //Retorna las mutaciones. 
            return res.status(200).send({
                mutations
            })
        });
    },
    getVHLTotal: (req, res)=>{
        //Obtiene todos los tipos de VHL que hay en la base de datos. 
        Mutation.find({},{"Case.VHL_type": 1}).distinct("Case.VHL_type").exec((err, vhls)=>{
            //Valida si existe la mutación
            if(err || vhls.length == 0){
                console.log("getVHLTotal No Data");
                return res.status(404).send({
                    message: "VHL don't exists"
                });
            }
            console.log("getVHLTotal Success");
            //Retorna la mutación. 
            return res.status(200).send({
                vhls
            })
        });
    },
    getEffectsTotal: (req, res)=>{
        //Obtiene todos los efectos de la base de datos. 
        Mutation.find({},{"Case.Disease.Effect": 1}).distinct("Case.Disease.Effect").exec((err, effects)=>{
            //Valida si existe la mutación
            if(err || effects.length == 0){
                console.log("Error / No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("Success");
            //Retorna la mutación. 
            return res.status(200).send({
                effects
            })
        });
    },
    //MODIFICAR BASE DE DATOS
    saveMutation: (req, res) =>{
        //Método para crear una nueva mutacion.
    },
    saveCase: (req, res) =>{
        //Método para añadir un nuevo caso a una mutación.
    }
}
module.exports = controller;