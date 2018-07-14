/**
 * @file Seism Search Controller
 * @author Aurelio vivas <aurelio.vivas@correounivalle.edu.co>
 * @version 0.1
 * 
 * Allows displaying a loading animation during
 * large load processes.
 *
 * @requires JQuery Library
 */


var LoaderService = function(){
  this.loader = $("#loader");
}


/**
 * Makes the laoder appear and disappear when required.
 */
LoaderService.prototype.toggle = function(){
  if (this.loader.children().length == 0){
    this.loader.html('<div class="loader col-sm-5 col-sm-offset-1"></div>');
  }else{
    this.loader.html('');
  } 
};