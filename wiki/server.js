var http = require('http')
var fs = require('fs')
var createHandler = require('github-webhook-handler')
var handler = createHandler({ path: '/webhook', secret: 'myhashsecret' })
var path = require("path");
var spawn = require( 'child_process' ).spawnSync;

function cloneRepo(){
  var ls = spawn( 'git', ["clone","https://github.com/Lascilab/Uvcluster", "/srv/gitbook"]);
  console.log( `stderr: ${ls.stderr.toString()}` );
  console.log( `stdout: ${ls.stdout.toString()}` );
}

function checkRepoFolder(){
  fs.access("/srv/gitbook", fs.F_OK, function(err) {
      if (err) {
          cloneRepo();
      }
  });
}

function pullRepo(){
  var ls = spawn( 'git', ["-C", "/srv/gitbook", "pull", "origin","master"]);
  console.log( `stderr: ${ls.stderr.toString()}` );
  console.log( `stdout:-${ls.stdout.toString()}-` );
  if(ls.stdout.toString().replace(/(\r\n|\n|\r)/gm,"").trim() !== "Already up-to-date.\n")
    genDoc();
}

function genDoc(){
  var ls = spawn( 'gitbook', ["install","/srv/gitbook"]);
  console.log( `stderr: ${ls.stderr.toString()}` );
  console.log( `stdout: ${ls.stdout.toString()}` );

  ls = spawn( 'gitbook', ["build","/srv/gitbook"]);
  console.log( `stderr: ${ls.stderr.toString()}` );
  console.log( `stdout: ${ls.stdout.toString()}` );
}

checkRepoFolder();

http.createServer(function (req, res) {
  handler(req, res, function (err) {
    res.statusCode = 404
    res.end('Lascilab')
  })
}).listen(3000)

handler.on('error', function (err) {
  console.error('Error:', err.message)
})

handler.on('push', function (event) {
  console.log('Received a push event for %s to %s',
    event.payload.repository.name,
    event.payload.ref)
    pullRepo();
})

handler.on('issues', function (event) {
  console.log('Received an issue event for %s action=%s: #%d %s',
    event.payload.repository.name,
    event.payload.action,
    event.payload.issue.number,
    event.payload.issue.title)
})
