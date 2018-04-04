(function() {
    var canvas, ctx;
    var height, width;
    var x = 500, y = 650;
    var xChange = 1, yChange = 1;
    var radius = 10;
    var platformHeight = 10, platformWidth = 125;
    var platformX = 437.5, platformY = 660;
    var right = false;
    var left = false;
    var zero;
    var brickRow = 6, brickColumn = 6;
    var brickWidth = 145, brickHeight = 25;
    var brickX = 20, brickY = 20;
    var bricks = [];
    var brickGap= 5;
    var timer = 4;
    var count;
    var loop;
    var brickloop;
    var c;
    var lives = 3;
    var score = 0;
    var paused = false;
    var started = false;
    var username;
    
    for(c = 0; c < brickColumn; c++) {
    bricks[c] = [];
    for(r=0; r < brickRow; r++) {
        bricks[c][r] = { x: 0, y: 0, status: 1 };
        }
    }
    
    document.addEventListener("DOMContentLoaded", init, false);

    function init() {
        canvas = document.getElementById("breakout");
        username = document.getElementById("navbarbutton").innerHTML;
        ctx = canvas.getContext("2d");
        height = canvas.height;
        width = canvas.width;
        window.addEventListener('keydown', keyDownHandler, false);
        window.addEventListener('keyup', keyUpHandler, false);
        window.addEventListener('keydown', start, false)
        ctx.font = "50px Arial";
        ctx.fillText ("Press space to start", 275, 350); 
    }
    
    function keyDownHandler (e) {
        if (e.keyCode == 39) { //Moves the platform to the right
            right = true    
        }
        else if (e.keyCode == 37) { //Moves the platform to the left
            left = true
        }
        else if (e.keyCode == 27 && paused == false && started == true) { //Escape keypress allows the user to pause the game
            clearInterval (loop);
            ctx.font = "30px Arial";
            ctx.fillText ("Game paused!", 400, 350);
            paused = true;
        }
        else if (e.keyCode == 27 && paused == true) { //Escape keypress unpauses the game provided the variable paused is True
            loop = window.setInterval (draw, 1);      
            paused = false;
        }
    }
    
    function keyUpHandler (e) {
        if (e.keyCode == 39) { //Stops the platform moving to the right
            right = false
        }
        else if (e.keyCode == 37) { //Stops the platform moving to the left
            left = false
        }
        else if (e.keyCode == 82) { //R keypress allows the user to restart the game once it has ended
            restart();
        }
    }
    
    function start(e) {
        if (e.keyCode == 32) { //Spacebar keypress gives the user a countdown before the game starts to allow for preparation
	    window.removeEventListener ('keydown', start);
            count = window.setInterval (countdown, 1000); //Does not have cooresponding keyUpHandler so as to avoid the button retriggering the countdown once the game has been finished
        }
    }
    
    function countdown () { //Countdown gives the user a countdown from 5 to prepare themselves for the game
        ctx.clearRect(0,0,1000, 700);
        timer = timer - 1;
        ctx.font = "250px Arial";
        ctx.fillText (+timer, 425, 450);
        if (timer == 0) {
            clearInterval (count);
            loop = window.setInterval (draw, 1);
            started = true;    
        }   
    }
   
    function draw () { //Draw is the main function to draw all the elements on the canvas; the ball, the bricks, the platform, the score and the lives *** STILL NEED TO IMPLEMENT BRICKFIELD ***
        ctx.clearRect(0, 0, width, height);
        platform();
        brick();
        brickCollisionDetection();
        x = x + xChange;
        y = y + yChange;
        ctx.beginPath();
        if ( x - radius < 0 ) {
            xChange = xChange * -1;
        } 
        else if ( x + radius > width ) {
            x = width - (x + radius - width) - radius;
            xChange = xChange * - 1;
        }
        
        if ( y - radius < 0 ) {

            yChange = yChange * - 1;
        }
        else if ( y - radius > height ) {
            if (lives == 1) {
                stop();
                lives = 0;          
            }
            else {
                lives --;
                x = 500;
                y = 650;
                platformX = 437.5;
                platformY = 660;
                xChange = 1;
                yChange = 1;
            }
        }
        if (y + radius > platformY && y - radius < platformY && (x + radius > platformX && x - radius < platformX + platformWidth)){
            yChange = -yChange;         
            if (x + radius <= (platformX + (platformWidth / 2))) { //This section modifes the xChange of the ball based upon how far from the middle of the platform the ball hits
                distance = (platformX + (platformWidth / 2) - x);
                multiplier = distance / (platformWidth / 2);
                if (xChange > 0) {
                    xChange = multiplier;
                }
                else if (xChange < 0) {
                    xChange = - (1 - multiplier)
                }             
            }
            else if (x - radius >= (platformX + (platformWidth / 2))) {
                distance = x  - (platformX + (platformWidth / 2));
                multiplier = distance / (platformWidth / 2);
                if (xChange < 0) {
                    xChange = - multiplier;
                }
                else if (xChange > 0) {
                    xChange = (1 - multiplier)
                }             
            }
        }
        ctx.arc(x, y, radius, 0, Math.PI*2, false);
        ctx.fillstyle = "#209BD0";
        ctx.fill();
        ctx.font = "30px Arial"
        ctx.fillText ("Lives = "+lives, 25, 25)
        ctx.fillText ("Score = "+score, 800, 25)
        ctx.closePath();
    }  
     
    function platform () {
        ctx.beginPath();
        if (right == true && platformX + platformWidth < width) {
            platformX += 3
        }

        if (left == true && platformX > 0) {
            platformX -= 3
        }
        ctx.rect(platformX, platformY, platformWidth, 15);
        ctx.fillstyle = "#209BD0";
        ctx.fill();        
        ctx.closePath();
    }
    
    function brick () {
        for (c = 0; c < brickColumn; c++) {
            for(r = 0; r < brickRow; r++) {
                if(bricks[c][r].status == 1) {
                var brickX = (r*(brickWidth+brickGap)) + 52.5;
                var brickY = (c*(brickHeight+brickGap)) + 35;
                bricks[c][r].x = brickX;
                bricks[c][r].y = brickY;
                ctx.beginPath();
                ctx.rect(brickX, brickY, brickWidth, brickHeight);
                ctx.fillstyle = "#209BD0";
                ctx.fill();
                ctx.closePath();
            }
          }
        }
    }
    
    function brickCollisionDetection() {
        for(c = 0; c < brickColumn; c++) {
            for(r = 0; r < brickRow; r++) {
            var b = bricks[c][r];
            if(b.status == 1) {
                if(x + radius > b.x && x - radius < b.x+brickWidth && y + radius > b.y && y - radius < b.y+brickHeight) {
                    yChange = yChange * - 1;
                    b.status = 0;
                    score = score + 5;
                }
                if(score == (brickRow*brickColumn) * 5) {
                    score = score + (150 * lives)
                    stop();
                    }
                }
            }
        }
    }

    function stop() {
     window.removeEventListener('keydown', keyDownHandler); //Did not remove keyup listener as it is needed so that the restart can work once the game has ended
     clearInterval (loop);
     window.alert("Game Over! Press R to restart the game or click the button below.");
     for (i = 0; i < 2; i ++) {
        var url = 'breakoutscore.py?username=' +username+ '&score=' + score;
        request = new XMLHttpRequest();
        request.addEventListener('readystatechange', handle_response, false);
        request.open('GET', url, true);
        request.send(null);
     }
   }
    
    function handle_response() {
      if ( request.readyState === 4 ) {
          if ( request.status === 200 ) {
              if ( request.responseText.trim() === 'success' ) {
              } 
              else  {d
              }
          }
      }
    }
    
     function restart () {
        window.location.reload(false);       
    }

})();