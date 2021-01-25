import { Case } from "./case";
export class Mutation{
    constructor(
        public _id: string,
        public Mutation: string,
        public Molecule: string,
        public Mutation_type: string,
        public Risk: string,
        public Protein_sequence: string,
        public DNA_sequence: string,
        public Case: Array<Case>
    ){}
}