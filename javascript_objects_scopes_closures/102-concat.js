#!/usr/bin/node
const fs = require('fs');
let coso = '';
coso = coso.concat(fs.readFileSync(process.argv[2]));
coso = coso.concat(fs.readFileSync(process.argv[3]));
fs.writeFileSync(process.argv[4], coso);
