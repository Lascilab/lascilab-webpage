var http = require('http')
var fs = require('fs')
var createHandler = require('github-webhook-handler')
var handler = createHandler({ path: '/', secret: 'myhashsecret' })
var path = require("path");
var exec = require('child_process').exec;

function cloneRepo(){
  exec( "git clone https://github.com/Lascilab/Uvcluster /srv/gitbook", function(error, stdout, stderr){
    if(error){
      console.error("No es posible clonar");
      return;
    }
    console.log("repositorio clonado")
  });
}

function checkRepoFolder(cb){
  fs.access("/srv/gitbook", fs.F_OK, function(err) {
      if (err) {
          console.error("repositorio inexistente")
          cloneRepo();
      }else{
        console.log("repositorio existente")
        pullRepo(function(err){
          genDoc(err)
        })
      }
  });
}

function pullRepo(){
  exec( "git -C /srv/gitbook pull origin master", function(error, stdout, stderr){
    if(error){
      console.error("No es posible hacer un pull");
      return;
    }
    console.log("Repositorio actualizado");
    if(stdout.toString().replace(/(\r\n|\n|\r)/gm,"").trim() !== "Already up-to-date.\n")
      genDoc();
  });
}

function genDoc(){
  exec("gitbook install /srv/gitbook", function(error, stdout, stderr){
    if(error){
      console.error("No es posible actualizar gitbook");
      return;
    }
    console.log("Gitbook actualizado");
    exec( "gitbook build /srv/gitbook /srv/html", function(error, stdout, stderr){
      if(error){
        console.error("No es posible construir gitbook");
        return;
      }
      console.log("Gitbook construido");
    });
  });
}

checkRepoFolder();
setInterval(checkRepoFolder, 1000*60*60*24)// cada 24h actualice

http.createServer(function (req, res) {
  handler(req, res, function (err) {
    res.statusCode = 404
    res.end('Lascilab')
    checkRepoFolder();
  })
}).listen(3000)
console.log("Servidor escuchando en el puerto 3000")

handler.on('error', function (err) {
  console.error('Error:', err.message)
})

handler.on('push', function (event) {
  console.log('Push recibido del repo %s para %s',
    event.payload.repository.name,
    event.payload.ref)
  checkRepoFolder();
})

handler.on('issues', function (event) {
  console.log('Received an issue event for %s action=%s: #%d %s',
    event.payload.repository.name,
    event.payload.action,
    event.payload.issue.number,
    event.payload.issue.title)
})
