"use strict"
var express = require("express");
var MutationController = require("../controllers/mutation");
var router = express.Router();
//Rutas
router.get("/getAll", MutationController.getAll);
router.get("/getFasta", MutationController.getFasta);
router.get("/getMutations", MutationController.getMutations);
router.get("/getMutation/:mutationName?", MutationController.getMutation);
router.get("/getCases/:mutationName?", MutationController.getCases);
router.get("/getVHLTotal", MutationController.getVHLTotal);
router.get("/getEffectsTotal", MutationController.getEffectsTotal);
router.get("/getTypesTotal", MutationController.getTypesTotal);
router.get("/getMutationsbyFilters/:vhlTypes?/:effects?", MutationController.getMutationsbyFilters);
router.get("/getDownloadsbyFilters/:vhlTypes?/:effects?/:mutationType?/:molecule?/:risk?", MutationController.getDownloadsbyFilters);
router.get("/getNumberbyFilters/:vhlTypes?/:effects?/:mutationType?/:molecule?/:risk?", MutationController.getNumberbyFilters);
router.get("/getMissense", MutationController.getMissense);
router.get("/getVHLVenn", MutationController.getVHLVenn);
router.get("/getEffvenn", MutationController.getEffVenn);
router.get("/getSubstitutionMatrix", MutationController.getSubstitutionMatrix);
router.get("/getSubstitutionPosition", MutationController.getSubstitutionPosition);
router.get("/getProteinSequence", MutationController.getProteinSequence);
router.get("/getSurveyVHL", MutationController.getSurkeyVHL);
router.get("/getHistPositions", MutationController.getHistPositions);
router.get("/getVarSurface", MutationController.getVarSurface);
module.exports = router;