//Commentare la riga qua sotto dopo aver verificato che ci sia l' alert e che quindi sia tutto collegato
//alert("Test di collegamento");
var score = 0;
var scoreText;
var increaseLife = 10;
var increaseStar = 100;

let config = {
    type: Phaser.AUTO,
    width: 1250,
    height: 700,
    backgroundColor: 0xff0000,
    parent: "game", //ID del div creato nel body!
    // pixelArt: true,

    //fisica
    physics: {
        default: "arcade",
        arcade: {
            gravity: { y: 300 },
            debug: true,
        },
    },

    //ciclo di vita di phaser
    scene: {
        preload: mioPreload, //si caricano le immagini che verranno usate
        create: mioCreate, //gestisco collisioni, tastiera...
        update: mioUpdate, //update contiene un loop infinito
    },
}

//START GAME
let gioco = new Phaser.Game(config)

//devo usare il comando function NON la funzione freccia "=()=>"
function mioPreload() {
    this.load.image("background", "./assets/background.png");
    this.load.image("spriteTom", "./assets/sprite_1.png");
    this.load.image("floor", "./assets/floor.png");
    this.load.image("wall", "./assets/wall.png");
    this.load.image("tube", "./assets/tube.png");
    this.load.image("tubeExit", "./assets/tubeExit.png");
    this.load.image("life", "./assets/life.png");
    this.load.image("star", "./assets/star.png");
}

function mioCreate() {
    //background
    this.add.image(620, 365, "background").setScale(2);
    //floor
    this.floor = this.physics.add.staticGroup({
        key: "floor",
        repeat: 2,
        setXY: { x: 290, y: 670, stepX: 400 },
        setScale: { x: 1, y: 1 },
    });
    //wall
    this.wall = this.physics.add.staticGroup({
        key: "wall",
        repeat: 2,
        setXY: { x: 970, y: 210, stepY: 110 },
        setScale: { x: 1, y: 1 },
    }),
    //tube
    this.tube = this.physics.add.sprite(70, 595, "tube").setScale(0.3);
    //tube exit
    this.tubeExit = this.add.image(1200, 50, "tubeExit").setScale(0.3);
    //score Text
    scoreText = this.add.text(16, 16, 'score: 0', { fontSize: '32px', fill: 'black' });
    //star
    this.star = this.physics.add.sprite(1125, 400, "star").setScale(0.2);
    //cuore
    this.life = this.physics.add.group({
        key: "life",
        repeat: 6,
        setXY: { x: 300, y: 400, stepX: 100 },
        setScale: { x: 2, y: 2 },
    });
    //sprite tom
    this.spriteTom = this.physics.add.sprite(600, 300, "spriteTom").setScale(2.5).setCollideWorldBounds(true); //"setCollideWorldBound(true)" serve per far fermare lo sprite quando tocca i bordi del rettangolo
    //tasto premuto
    this.mioTasto = this.input.keyboard.createCursorKeys(); //memorizza il tasto premuto nella variabile "mioTasto", posso controllare solo UP ARROW, DOWN ARROW, LEFT ARROW, RIGHT ARROW, TAB e SPACE. 
    
    
    //---- ANIMAZIONI ----
    /*
    this.animation = this.tweens.createTimeLine();
    this.animation.add({
        targets:[this.star],
        duration:3000,
        ease:"elastic",
        y:300,
    }),
    this.animation.play();
    */

    //----  COLLISIONI GRAVITÀ  ----
    //collisione tom/life/tube/wall - floor
    this.physics.add.collider(this.floor, [this.life, this.spriteTom, this.tube, this.wall, this.star]);
    //collisione tom - muro
    this.physics.add.collider(this.wall, this.spriteTom);

    //----  COLLISIONI GIOCO  ----
    //collisione tom - cuore (overlap serve a farlo "passare attraverso" senza cambiare la traiettoria)
    this.physics.add.overlap(this.spriteTom, this.life, collectLife, null, this);
    //collisione tom - star
    this.physics.add.overlap(this.spriteTom, this.star, collectStar, null, this);
    //collisione tom - tubo
    this.physics.add.overlap(this.spriteTom, this.tube, tube, null, this);
}

function mioUpdate(time, delta) {
    //RIGHT ARROW
    if (this.mioTasto.right.isDown) {
        this.spriteTom.setVelocityX(200);
    } else {
        this.spriteTom.setVelocityX(0);
    }
    //LEFT ARROW
    if (this.mioTasto.left.isDown) {
        this.spriteTom.setVelocityX(-200);
    }
    //SPACE
    if (Phaser.Input.Keyboard.JustDown(this.mioTasto.space)) {
        this.spriteTom.setVelocityY(-200);
    }
    
}

//funzione collect life --> add score
function collectLife(sprite, life) {
    life.disableBody(true, true);
    score += increaseLife;
    scoreText.setText('Score: ' + score);
}

//funzione collect star --> add score
function collectStar(sprite, star) {
    star.disableBody(true, true);
    score += increaseStar;
    scoreText.setText('Score: ' + score);
}

//funzione tube --> move Tom
function tube(sprite, tube) {
    this.spriteTom.x = 1100;
    this.spriteTom.y = 50;
}