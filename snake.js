(function() {

    var canvas;
    var ctx;
    var width;
    var height;
    var loop;
    var xposition = 0;
    var yposition = 0;
    var lastx = 0;
    var lasty = 0;
    var prevx = 0;
    var prevy = 0;
    var body = [];
    var score = 20;
    var foodx = -10;
    var foody = 0;
    var right = false;
    var left = false;
    var up = false;
    var down = false;
    var timer = 4;
    var count;
    var paused = false;
    var started = false;
    var username;
    var request;
    
    document.addEventListener('DOMContentLoaded', init, false);

    function init() {
      canvas = document.getElementById('snake');
      username = document.getElementById("navbarbutton").innerHTML;
      ctx = canvas.getContext('2d');
      width = canvas.width;
      height = canvas.height;
      xposition = getRandomNumber(0,(width-10)/10)*10;
      yposition = getRandomNumber(0,(height-10)/10)*10;
      window.addEventListener('keydown',move,false);
      window.addEventListener('keyup',keyUpHandler,false);
      window.addEventListener('keydown', start, false)
      ctx.font = "30px Arial";
      ctx.fillStyle = "white";
      ctx.fillText ("Press space to start", 125, 275); 
    } 

    function move(e){
     if (e.keyCode === 37 && right === false){
      right=false;
      up=false;
      down=false;
      left=true;
        } 
     else if (e.keyCode === 38 && down === false){
      up=true;
      down=false;
      left=false;
      right=false;
        } 
     else if (e.keyCode === 39 && left === false){
      right=true;
      up=false;
      down=false;
      left=false;
        } 
     else if (e.keyCode === 40 && up === false){
      right=false;
      up=false;
      down=true;
      left=false;  
        }
     else if (e.keyCode == 27 && paused == false && started == true) { //Escape keypress allows the user to pause the game
      clearInterval (loop);
      ctx.font = "30px Arial";
      ctx.fillStyle = "white";
      ctx.fillText ("Game paused!", 155, 275);
      paused = true;
        }
    else if (e.keyCode == 27 && paused == true) { //Escape keypress unpauses the game provided the variable paused is True
      loop = window.setInterval (draw, 60);      
      paused = false;
        }
    }
    
    function keyUpHandler(e) {
        if (e.keyCode == 82) { //R keypress allows the user to restart the game once it has ended. Explicitly put this as keyup and did not remove the listener so the game could be restarted without giving the user movement of the snake
            restart()
        }
    }
    
    function start(e) {
        if (e.keyCode == 32) { //Spacebar keypress gives the user a countdown before the game starts to allow for preparation
	    window.removeEventListener ('keydown', start);
            count = window.setInterval (countdown, 1000); //Does not have cooresponding keyUpHandler so as to avoid the button retriggering the countdown once the game has been finished
        }
    }
    
    function countdown () { //Countdown gives the user a countdown from 5 to prepare themselves for the game
        ctx.clearRect(0,0,500, 500);
        timer = timer - 1;
        ctx.font = "100px Arial";
        ctx.fillStyle = "white";
        ctx.fillText (+timer, 225, 275);
        if (timer == 0) {
            clearInterval(count);
            loop = window.setInterval (draw, 60);
            started = true;    
        }   
    }
    
    function draw(){
      ctx.clearRect(0,0,width,height)
      ctx.fillStyle = 'lime';
      if (body.length > 0){
	var tail = {
	 x : xposition,
	 y : yposition 
	};
	body.unshift (tail);
	body.pop();
	for (i = 0; i < body.length; i++){
	 ctx.fillRect(body[i].x, body[i].y, 10, 10) 
	};
      }
      if (down === true){
	yposition += 10;
      } else if (left === true){
	xposition -= 10;
      } else if (right === true){
	xposition += 10;
      } else if (up === true){
	yposition -= 10;
      }
      if (xposition < 0 || xposition >= width || yposition < 0 || yposition >= height){
      stop(); 
     }
     else if (body.length > 3)
     for (i = 0; i < body.length; i++){
      if (xposition === body[i].x && yposition === body[i].y){
	stop();
      }
     }
      food();
      ctx.fillRect(xposition,yposition, 10, 10);
      ctx.fillStyle = "aqua";
      ctx.fillRect(foodx,foody, 10, 10);
      drawScore();
    }
    
    function drawScore() {
    ctx.font = "16px Arial";
    ctx.fillStyle = "white";
    ctx.fillText("Score: "+score, 8, 20);
    }
    
    function food(){
     if (foodx < 0){
      foodx = getRandomNumber(0,(width-10)/10)*10;
      foody = getRandomNumber(0,(height-10)/10)*10;
     } else if (foodx === xposition && foody === yposition){
      foodx = getRandomNumber(0,(width-10)/10)*10;
      foody = getRandomNumber(0,(height-10)/10)*10;
      score+=1
      extend()
     }
    }
    
    function extend(){
     part = {
      x : lastx,
      y : lasty
     };
     body.push("part")
    }
    
    function stop(){
     clearInterval(loop);
     window.removeEventListener('keydown', move);
     window.alert("Game Over! Press R to restart the game or click the button below. Your score was "+score);
     for (i = 0; i < 2; i ++){
        var url = 'snakescore.py?username='+username+'&score='+score;
        request = new XMLHttpRequest();
        request.open('GET', url, true);
        request.send(null);
     }
   }
    
    function getRandomNumber(min, max) {
      return Math.round(Math.random() * (max - min)) + min;
    }
    
    function restart () {
        window.location.reload(false);       
    }
})();