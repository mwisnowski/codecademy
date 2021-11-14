// Returns a random DNA base
const returnRandBase = () => {
  const dnaBases = ['A', 'T', 'C', 'G']
  return dnaBases[Math.floor(Math.random() * 4)]
};

// Returns a random single stand of DNA containing 15 bases
const mockUpStrand = () => {
  const newStrand = []
  for (let i = 0; i < 15; i++) {
    newStrand.push(returnRandBase())
  }
  return newStrand
};

const pAequorFactory = (number, bases) => {

  return {
    specimenNum: number,
    dna: bases,

    mutate(){
      let mutateBase = Math.floor(Math.random() * this.dna.length);
      let mutateRandomize = returnRandBase();
      while (!this.dna === this.dna.splice(mutateBase, 1, mutateRandomize)) {
        this.dna.splice(mutateBase, 1, mutateRandomize);
      }
      return this.dna;
    },
    compareDNA(pAequor){

      let count = 0;
      for(let i = 0; i < this.dna.length; i++){
        const initBase = this.dna[i];
        const reInitBase = pAequor.dna[i];
        if(this.initBase === reInitBase) {
          count++;
        }
      }
      return `The total identical base count is ${count}. Specimen #1 and Specimen #2 have ${((count /this.dna.length) * 100).toFixed(2)}% DNA in common.`;
    },
    willLikelySurvive() {
      let count = 0;

      for (let i = 0; i < this.dna.length; i++){
        const initBase = this.dna[i];
        if (initBase === "C" || initBase === "G") {
          count++
        }
      }
      if (count >= 9) {
        return true;
      } else {
        return false;
      }
    },
    complementStrand() {
      let complementaryStrandArray = [];
      const dnaBases = ['A', 'T', 'C', 'G'];
      for (let i =0; i < this.dna.length; i++) {
        const base = this.dna[i];

        if (base === dnaBases[0]) {
          complementaryStrandArray.push(dnaBases[1]);
        } else if (base === dnaBases[1]) {
          complementaryStrandArray.push(dnaBases[0]);
        } else if (base === dnaBases[2]) {
          complementaryStrandArray.push(dnaBases[3]);
        } else if (base === dnaBases[3]) {
          complementaryStrandArray.push(dnaBases[2]);
        } else {
          complementaryStrandArray.push("error");
        }
      }
      return complementaryStrandArray;
    }
  };
};

const createSurvivablePAequorArray = (amount, startingSpecimenNumber) => {
let count = startingSpecimenNumber;
let array = [];
while (count < amount + startingSpecimenNumber) {
  let newPAequor = pAequorFactory(count, mockUpStrand());
  if (newPAequor.willLikelySurvive()) {
    array.push(newPAequor);
    count++;
  }
}
return array;
};

// create 30 high survivability strains of p.aequor
let subjectInstances = createSurvivablePAequorArray(30, 210);
//console.log(subjectInstances)

// bonus create complementary strands test
let testSubject10 = pAequorFactory(10, mockUpStrand());
console.log(testSubject10.complementStrand());
