var box = document.getElementById('box');
var span = box.getElementsByTagName('span');


var redBall = [];//空数组 用来存放红球
for(var i=0;i<6;i++){
    var rand = Math.floor(Math.random()*33+1);
    if(redBall.indexOf(rand) == -1){
        redBall.push(rand);
    }else{
        i--;
    }
}

for(var i=0;i<redBall.length;i++){
    //跟下一个球进行比较
    for(var j=i+1;j<redBall.length;j++){
        if(redBall[i]>redBall[j]){
            var temp = redBall[i];
            redBall[i] = redBall[j];
            redBall[j] = temp;
        }
    }
}

var blueBall = Math.floor(Math.random()*16+1);
redBall.push(blueBall);

for(var i=0;i<span.length;i++){
    span[i].innerHTML = redBall[i];
}