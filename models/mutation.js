"use strict"
var mongoose = require("mongoose");
var Schema = mongoose.Schema;
var MutationSchema = Schema({
});
module.exports = mongoose.model("Mutation", MutationSchema, "Mutation");