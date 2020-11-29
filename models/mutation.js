"use strict"
var mongoose = require("mongoose");
var Schema = mongoose.Schema;
var MutationSchema = Schema({
    mutation: String,
    mutation_type: String
});
module.exports = mongoose.model("Mutation", MutationSchema);