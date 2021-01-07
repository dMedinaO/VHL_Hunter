"use strict"
var express = require("express");
var MutationController = require("../controllers/mutation");
var ComplexController = require("../controllers/complex");
var router = express.Router();
//Rutas
router.get("/getAll", MutationController.getAll);
router.get("/getFasta", MutationController.getFasta);
router.get("/getMutations", MutationController.getMutations);
router.get("/getMutation/:mutationName?", MutationController.getMutation);
router.get("/getCases/:mutationName?", MutationController.getCases);
router.get("/getEffects/:mutationName?", MutationController.getEffects);
router.get("/getVHL/:mutationName?", MutationController.getVHL);
router.get("/getMutationsbyEffect/:effect?", MutationController.getMutationsbyEffect);
router.get("/getMutationsbyRisk/:risk?", MutationController.getMutationsbyRisk);
router.get("/getMutationsbyType/:mutationType?", MutationController.getMutationsbyType);
router.get("/getMutationsbyVHL/:vhlType?", MutationController.getMutationsbyVHL);
router.get("/getMutationsbyBoth/:vhlType?/:effect?", MutationController.getMutationbyBoth);
router.get("/getVHLTotal", MutationController.getVHLTotal);
router.get("/getEffectsTotal", MutationController.getEffectsTotal);
router.get("/getTypesTotal", MutationController.getTypesTotal);
router.get("/getMutationsbyFilters/:vhlTypes?/:effects?", MutationController.getMutationsbyFilters);
router.get("/getDownloadsbyFilters/:vhlTypes?/:effects?/:mutationType?/:molecule?/:risk?", MutationController.getDownloadsbyFilters);
module.exports = router;