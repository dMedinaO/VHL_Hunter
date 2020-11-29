"use strict"
var express = require("express");
var MutationController = require("../controllers/mutation");
var ComplexController = require("../controllers/complex");
var router = express.Router();
//Rutas
//Mutaciones sencillas
router.get("/getMutation/:mutationName?", MutationController.getMutation);
router.get("/getCases/:mutationName?", MutationController.getCases);
router.get("/getEffects/:mutationName?", MutationController.getEffects);
router.get("/getVHL/:mutationName?", MutationController.getVHL);
router.get("/getMutationsbyEffect/:effect?", MutationController.getMutationsbyEffect);
router.get("/getMutationsbyRisk/:risk?", MutationController.getMutationsbyRisk);
router.get("/getMutationsbyType/:mutationType?", MutationController.getMutationsbyType);
router.get("/getMutationsbyVHL/:vhlType?", MutationController.getMutationsbyVHL);
router.get("/getVHLTotal/", MutationController.getVHLTotal);
router.get("/getEffectsTotal/", MutationController.getEffectsTotal);
//Mutaciones Complejas
router.get("/getComplex/:mutationName?", ComplexController.getComplex);
router.get("/getCouples/:mutationName?", ComplexController.getCouples);
router.get("/getCaseCogeuples/:mutationName?", ComplexController.getCaseCouples);//En proceso

module.exports = router;