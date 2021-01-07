import {Disease} from "./disease";
import {Reference} from "./reference";
export class Case{
    constructor(
        public Disease: Array<Disease>,
        public VHL_type: Array<string>,
        public Reference: Array<Reference>
    ){}
}