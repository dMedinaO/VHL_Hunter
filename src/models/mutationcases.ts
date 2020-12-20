import {Case} from "./case";
export class MutationCases{
    constructor(
        public Mutation: string,
        public Molecule: string,
        public Mutation_type: string,
        public Case: Array<Case>
    ){}
}