(function() {
    var canvas;
    var ctx;
    var height;
    var width;
    var x = 500, y = 375;
    var xChange = 1, yChange = -1;
    var radius = 10;
    var platformHeight =150, platformWidth = 10;
    var platform1X = 20, platform1Y = 300;
    var platform2X = 970, platform2Y = 300;
    var up = false;
    var down = false;
    var w = false;
    var s = false;
    var timer = 4;
    var loop;
    var leftlives = 5;
    var rightlives = 5;
    var winner;
    var score = 0;
    var paused = false;
    var started = false;
    var username;
    
    document.addEventListener("DOMContentLoaded", init, false);

    function init() {
        canvas = document.getElementById("hardsinglepong");
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
        if (e.keyCode == 40) { //Moves the left platform up
            down = true;
            console.log ("Down")
        }
        else if (e.keyCode == 38) { //Moves the left platform down
            up = true;
        }
        if (e.keyCode == 87) { //Moves the right platform up
            w = true;
        }
        else if (e.keyCode == 83) { //Moves the right platform down
            s = true;
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
        if (e.keyCode == 40) { //Stops the left platform moving up
            down = false;
        }
        else if (e.keyCode == 38) { //Stops the left platform moving down
            up = false;
        }
        if (e.keyCode == 87) { //Stops the right platform moving up
            w = false;
        }
        else if (e.keyCode == 83) { //Stops the right platform moving down
            s = false;
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
            clearInterval(count);
	    loop = window.setInterval (draw, 1)
            started = true;
        }   
    }
   
    function draw () { //Draw is the main function to draw all the elements on the canvas; the ball, the bricks, the platform, the score and the lives *** STILL NEED TO IMPLEMENT SCORE AND LIVES ***
        ctx.clearRect(0, 0, width, height);
        platform1();
        platform2();
        x = x + xChange;
        y = y + yChange;
        ctx.beginPath();
        if ( x + radius < 0 ) {
            score += 100;
            if (leftlives == 1) {
                winner = "You win! "
                score = score + (75 * rightLives);
                stop();
                leftlives = 0;   
            }
            else{
                leftlives --;
                x = 500;
                y = 375;
                xChange = 1;
                yChange = 1;
                platform1X = 20, platform1Y = 300;
                platform2X = 970, platform2Y = 300;
            }
        } 
        else if ( x - radius > width ) {
            if (rightlives == 1) {
                winner = "The computer wins! "
                stop();
                rightlives = 0;               
            }
            else{
                rightlives --;
                x = 500;
                y = 375;
                xChange = -1;
                yChange = -1;
                platform1X = 20, platform1Y = 300;
                platform2X = 970, platform2Y = 300;
            }
        }
        
        if ( y - radius < 0 ) {
            y = y * -1 + radius;
            yChange = yChange * - 1;
        }
        else if ( y + radius > height ) {
            y = height - (y + radius - height) - radius;
            yChange = yChange * -1;
        }
        if (x + radius > platform1X && x - radius < platform1X && (y > platform1Y && y < platform1Y + platformHeight)){
            xChange = -xChange;
            xChange = xChange * 1.05;
            yChange = yChange * 1.05;
        }
        if (x - radius < platform2X && x + radius > platform2X && (y > platform2Y && y < platform2Y + platformHeight)){
            xChange = -xChange;
            xChange = xChange * 1.05;
            yChange = yChange * 1.05;
            score += 5;
        }
        ctx.arc(x, y, radius, 0, Math.PI*2, false);
        ctx.fillstyle = "#F39276";
        ctx.fill();
        ctx.font = "30px Arial";
        ctx.fillText ("Lives = "+leftlives, 25, 45);
        ctx.fillText ("Lives = "+rightlives, 850, 45);
        ctx.fillText ("Score = "+score, 425, 50)
        ctx.closePath();
    }  
     
    function platform1 () {
        ctx.beginPath();
        platform1Y += yChange * 0.8;
        ctx.rect(platform1X, platform1Y, platformWidth, platformHeight);
        ctx.fillstyle = "green";
        ctx.fill();        
        ctx.closePath();
    }
    
    function platform2 () {
        ctx.beginPath();
        if (down == true && platform2Y + platformHeight < height) {
            platform2Y += 3
        }
        if (up == true && platform2Y > 0) {
            platform2Y -= 3
        }
        ctx.rect(platform2X, platform2Y, platformWidth, platformHeight);
        ctx.fillstyle = "green";
        ctx.fill();        
        ctx.closePath();
    }

    function stop() {
     window.removeEventListener('keydown', keyDownHandler); //Did not remove keyup listener as it is needed so that the restart can work once the game has ended
     clearInterval (loop);
     window.alert(winner+"Press R to restart the game or click the button below. Your score was "+score);
     for (i = 0; i < 2; i ++) {
        var url = 'hardpongscore.py?username=' +username+ '&score=' + score;
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
              else  {
              }
          }
      }
    }
    
     function restart () {
        window.location.reload(false);       
    }
    
})();