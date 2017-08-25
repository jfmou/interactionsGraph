# interactionsGraph

`npm install` pour installer le projet.

Le projet est composé : 
* d'un parser qui converti un fichier csv exporté depuis google drive en fichier json de graph : `node parser.js`
* d'un server static (accessible via http://localhost:3000) permettant de servir le json de graph afin d'être rendu coté client en tant que [force-directd graph via d3.js](https://bl.ocks.org/mbostock/4062045) :  `node server.js` (http://localhost:3000)
