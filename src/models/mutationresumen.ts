export class MutationResumen{
    constructor(
        public _id: string,
        public Mutation: string,
        public Molecule: string,
        public Mutation_type: string,
        public Reports: number,
        public Risk: string
    ){}
}