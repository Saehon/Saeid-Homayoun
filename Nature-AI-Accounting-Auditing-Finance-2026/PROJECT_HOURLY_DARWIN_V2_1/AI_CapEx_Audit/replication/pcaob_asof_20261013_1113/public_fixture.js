// Public-only PCAOB inspection audit fixture (2024 inspection reports).
const firms={Deloitte:{partIA:9,reviewed:63},EY:{partIA:18,reviewed:64},PwC:{partIA:10,reviewed:64}};
for(const [name,x] of Object.entries(firms)){if(!(x.partIA>=0&&x.partIA<=x.reviewed))throw Error(name);console.log(name,x.partIA/x.reviewed);}
