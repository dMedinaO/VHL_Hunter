import {Disease} from "./disease";
export class Case{
    constructor(
        public Disease: Array<Disease>,
        public VHL_type: Array<string>,
        public Pubmed_ID: Array<string>
    ){}
}