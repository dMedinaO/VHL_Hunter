"use strict"
var Mutation = require("../models/mutation");
var path = require("path");
var fs = require("fs");
const { query } = require("express");
const csv = require('csv-parser');
const { exception } = require("console");
var controller = {
    getAll: (req, res) => {
        Mutation.find({}).exec((err, mutations) => {
            //Valida si existe la mutación en la colección. 
            if (err || mutations.length == 0) {
                console.log("getAll No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getAll Success");
            //Retorna la mutación. 
            return res.status(200).send({
                mutations
            })
        })
    },
    getFasta: (req, res) => {
        //Obtiene la mutación y sus secuencias asociadas. 
        Mutation.aggregate([
            {
                $project: {
                    Mutation: 1,
                    DNA_sequence: 1,
                    Protein_sequence: 1,
                }
            }]
        ).exec((err, mutations) => {
            if (err || mutations.length == 0) {
                console.log("getFasta No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getFasta Success");
            return res.status(200).send({
                mutations
            })
        });
    },
    getMutations: (req, res) => {
        //Obtiene las mutaciones, con un recuento de sus casos asociados. 
        Mutation.aggregate([{
            $project: {
                Mutation: 1,
                Molecule: 1,
                Mutation_type: 1,
                Risk: 1,
                Protein_sequence: 1,
                DNA_sequence: 1,
                Reports: { $cond: { if: { $isArray: "$Case" }, then: { $size: "$Case" }, else: 0 } }
            }
        }]).exec((err, mutation) => {
            if (err || mutation.length == 0) {
                console.log("getMutations No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getMutations Success");
            return res.status(200).send({
                mutation
            })
        });
    },
    getMutation: (req, res) => {
        //Método para obtener toda la información de la mutación especificada como parámetro (nombre). 
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación correctamente. 
        if (!mutationName || mutationName == undefined) {
            if (!mutationName) {
                console.log("getMutation Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({ "Mutation": mutationName }).exec((err, mutation) => {
            //Valida si existe la mutación en la colección. 
            if (err || mutation.length == 0) {
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
    getCases: (req, res) => {
        //Retorna los casos en los que se ha asociado la mutación ingresada
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación. 
        if (!mutationName || mutationName == undefined) {
            if (!mutationName) {
                console.log("getCases Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({ "Mutation": mutationName }, { "Case": 1 }).exec((err, cases) => {
            //Valida si existe la mutación
            if (err || cases.length == 0) {
                console.log("getCases No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getCases Success");
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
        if (!mutationName || mutationName == undefined) {
            if (!mutationName) {
                console.log("getEffects Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({ "Mutation": mutationName }, { "Case.Disease.Effect": 1 }).distinct("Case.Disease.Effect").exec((err, effects) => {
            //Valida si existe la mutación
            if (err || effects.length == 0) {
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
    getVHL: (req, res) => {
        //Obtiene los tipos de VHL de una mutación. 
        //Parámetros llegan por params. 
        var mutationName = req.params.mutationName;
        //Valida si ingresó nombre de la mutación. 
        if (!mutationName || mutationName == undefined) {
            if (!mutationName) {
                console.log("getVHL Error")
                return res.status(404).send({
                    message: "Mutation isn't defined"
                });
            }
        }
        Mutation.find({ "Mutation": mutationName }, { "Case.VHL_type": 1 }).distinct("Case.VHL_type").exec((err, vhl) => {
            //Valida si existe la mutación en la colección
            if (err || vhl.length == 0) {
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
    getVHLTotal: (req, res) => {
        //Obtiene todos los tipos de VHL que hay en la base de datos. 
        Mutation.find({}, { "Case.VHL_type": 1 }).distinct("Case.VHL_type").exec((err, vhls) => {
            //Valida si existe la mutación
            if (err || vhls.length == 0) {
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
    getEffectsTotal: (req, res) => {
        //Obtiene todos los efectos de la base de datos. 
        Mutation.find({}, { "Case.Disease.Effect": 1 }).distinct("Case.Disease.Effect").exec((err, effects) => {
            //Valida si existe la mutación
            if (err || effects.length == 0) {
                console.log("Error / No Data");
                return res.status(404).send({
                    message: "Error, no effects"
                });
            }
            console.log("getEffectsTotal Success");
            //Retorna la mutación. 
            return res.status(200).send({
                effects
            })
        });
    },
    getTypesTotal: (req, res) => {
        Mutation.find({}, { "Mutation_type": 1 }).distinct("Mutation_type").exec((err, types) => {
            if (err || types.length == 0) {
                console.log("Error / No Data");
                return res.status(404).send({
                    message: "Error, no mutation types"
                });
            }
            console.log("getEffectsTotal Sucess");
            //Retorna la mutación. 
            return res.status(200).send({
                types
            })
        })
    },
    getMutationsbyFilters: (req, res) => {
        var vhlTypes = req.params.vhlTypes;
        var effects = req.params.effects;
        var filters = []
        if (vhlTypes != "undefined") {
            vhlTypes = vhlTypes.split(",")
            for (let i = 0; i < vhlTypes.length; i++) {
                filters.push({ "Case.VHL_type": vhlTypes[i] })
            }
        }
        if (effects != "undefined") {
            effects = effects.split(",")
            for (let i = 0; i < effects.length; i++) {
                filters.push({ "Case.Disease.Effect": effects[i] })
            }
        }
        var match;
        if (vhlTypes == "undefined" && effects == "undefined") {
            match = { $and: [{}] }
        }
        else {
            match = { $and: filters }
        }
        Mutation.aggregate([
            { $match: match },
            {
                $project: {
                    Mutation: 1,
                    Molecule: 1,
                    Mutation_type: 1,
                    Risk: 1,
                    Protein_sequence: 1,
                    DNA_sequence: 1,
                    Reports: { $cond: { if: { $isArray: "$Case" }, then: { $size: "$Case" }, else: 0 } }
                }
            }]).exec((err, mutations) => {
                if (err || mutations.length == 0) {
                    console.log("Error / No Data");
                    return res.status(200).send({
                        message: "No data available"
                    });
                }
                console.log("getMutationsbyFilters Success");
                return res.status(200).send({
                    mutations
                })
            })
    },
    getDownloadsbyFilters: (req, res) => {
        var vhlTypes = req.params.vhlTypes;
        var effects = req.params.effects;
        var mutationType = req.params.mutationType;
        var molecule = req.params.molecule;
        var risk = req.params.risk;
        var filters = []
        if (vhlTypes != "undefined") {
            vhlTypes = vhlTypes.split(",")
            for (let i = 0; i < vhlTypes.length; i++) {
                filters.push({ "Case.VHL_type": vhlTypes[i] })
            }
        }
        if (effects != "undefined") {
            effects = effects.split(",")
            for (let i = 0; i < effects.length; i++) {
                filters.push({ "Case.Disease.Effect": effects[i] })
            }
        }
        if (mutationType != "undefined") {
            filters.push({ "Mutation_type": mutationType });
        }
        if (molecule != "undefined") {
            filters.push({ "Molecule": molecule });
        }
        if (risk != "undefined") {
            filters.push({ "Risk": risk });
        }
        var match;
        if (vhlTypes == "undefined" && effects == "undefined" && mutationType == "undefined" && molecule == "undefined" && risk == "undefined") {
            match = { $and: [{}] }
        }
        else {
            match = { $and: filters }
        }
        Mutation.find(match).exec((err, mutations) => {
            if (err || mutations.length == 0) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            }
            console.log("getDownloadsbyFilters Success");
            return res.status(200).send({
                message: "Downloading",
                mutations
            })
        })
    },
    getNumberbyFilters: (req, res) => {
        var vhlTypes = req.params.vhlTypes;
        var effects = req.params.effects;
        var mutationType = req.params.mutationType;
        var molecule = req.params.molecule;
        var risk = req.params.risk;
        var filters = []
        if (vhlTypes != "undefined") {
            vhlTypes = vhlTypes.split(",")
            for (let i = 0; i < vhlTypes.length; i++) {
                filters.push({ "Case.VHL_type": vhlTypes[i] })
            }
        }
        if (effects != "undefined") {
            effects = effects.split(",")
            for (let i = 0; i < effects.length; i++) {
                filters.push({ "Case.Disease.Effect": effects[i] })
            }
        }
        if (mutationType != "undefined") {
            filters.push({ "Mutation_type": mutationType });
        }
        if (molecule != "undefined") {
            filters.push({ "Molecule": molecule });
        }
        if (risk != "undefined") {
            filters.push({ "Risk": risk });
        }
        var match;
        if (vhlTypes == "undefined" && effects == "undefined" && mutationType == "undefined" && molecule == "undefined" && risk == "undefined") {
            match = { $and: [{}] }
        }
        else {
            match = { $and: filters }
        }
        Mutation.count(match).exec((err, cant) => {
            if (err || cant.length == 0) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            }
            return res.status(200).send({
                message: "Downloading",
                cant
            })
        })
    },
    getMissense: (req, res) => {
        Mutation.find({ "Mutation_type": "Missense" }).exec((err, mutation) => {
            //Valida si existe la mutación en la colección. 
            if (err || mutation.length == 0) {
                console.log("getMissense No Data");
                return res.status(404).send({
                    message: "Mutation don't exists"
                });
            }
            console.log("getMissense Success");
            //Retorna la mutación. 
            return res.status(200).send({
                mutation
            })
        });
    },
    getVHLVenn: (req, res) => {
        fs.readFile("datasets/vhl-venn.json", (err, data) => {
            if (err) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            } else {
                console.log("getVHLVenn Success")
                return res.status(200).send({
                    data: JSON.parse(data)
                })
            }
        });
    },
    getEffVenn: (req, res) => {
        fs.readFile("datasets/eff-venn.json", (err, data) => {
            if (err) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            } else {
                console.log("getEffVenn Success")
                return res.status(200).send({
                    data: JSON.parse(data)
                })
            }
        });
    },
    getSubstitutionMatrix: (req, res) => {
        var arreglo = []
        fs.createReadStream('datasets/SubstitutionMatriz.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row).map(function (item) {
                    return parseInt(item, 10);
                }));
            })
            .on('end', () => {
                return res.status(200).send({
                    data: arreglo
                })
            });
    },
    getSubstitutionPosition: (req, res) => {
        var arreglo = []
        fs.createReadStream('datasets/SubstitutionPosition.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row).map(function (item) {
                    return parseInt(item, 10);
                }));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    },
    getProteinSequence: (req, res) => {
        fs.readFile("sequences/pvhl.str", "utf8", (err, sequence) => {
            if (err) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            } else {
                console.log(sequence)
                return res.status(200).send({
                    sequence
                })
            }
        });
    },
    getSankeyVHL: (req, res)=>{
        var arreglo = []
        fs.createReadStream('datasets/SurveyVHL.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    }, 
    getSankeyEff: (req, res)=>{
        var arreglo = []
        fs.createReadStream('datasets/SankeyEff.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    }, 
    getHistPositions: (req, res)=>{
        var arreglo = []
        fs.createReadStream('datasets/hist-pos.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row).map(function (item) {
                    return parseInt(item, 10);
                }));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    },
    getVarSurface: (req, res)=>{
        var arreglo = []
        fs.createReadStream('datasets/surface-var.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row).map(function (item) {
                    return parseInt(item, 10);
                }));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    },
    getAllJson: (req, res)=>{
        var file = "datasets/AllDataJson.json";
        res.download(file);
    },
    getHistVHL: (req, res)=>{
        var arreglo = []
        fs.createReadStream('datasets/histVHL.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    }, 
    getHistEff: (req, res)=>{
        var arreglo = []
        fs.createReadStream('datasets/histEff.csv')
            .pipe(csv()).on('data', (row) => {
                arreglo.push(Object.values(row));
            })
            .on('end', () => {
                console.log("Success")
                return res.status(200).send({
                    data: arreglo
                })
            });
    }, 
    getResumeVHL: (req, res)=>{
        fs.readFile("datasets/resumeDataVHL.json", (err, data) => {
            if (err) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            } else {
                console.log("getResumeVHL Success")
                return res.status(200).send({
                    data: JSON.parse(data)
                })
            }
        });
    }, 
    getresumeEff: (req, res)=>{
        fs.readFile("datasets/resumeDataEff.json", (err, data) => {
            if (err) {
                console.log("Error / No Data");
                return res.status(200).send({
                    message: "No data available"
                });
            } else {
                console.log("getResumeEff Success")
                return res.status(200).send({
                    data: JSON.parse(data)
                })
            }
        });
    }, 
}
module.exports = controller;