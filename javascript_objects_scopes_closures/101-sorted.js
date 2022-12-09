const dict = requiere('./101-data.js').dict;
let mapMe = {};
for (const [key, value] of dict) {
    mapMe.set(key, value)
}