![](https://www.shieldsquare.com/web/wp-content/uploads/2014/12/reCaptcha-ShieldSquare.gif)

## How it works?

![alt tag](https://media.discordapp.net/attachments/671809375807209472/724376452962844692/Untitled_Diagram.png)

Basically what it does is that it checks if the site page source has an iframe 
embedded in it or not if it has one then it moves on to the audio challenge of the recaptcha,
in there it downloads the audio file provided by the recaptcha, then passes it through google's voice recognition api,
and enters the output text obtained from the speech as the answer to the audio challenge , and else it terminates. Thats the whole story.

## How to prevent it from bypassing

Basically all it does is recognize the voice and enters it as an answer so if the voice is distorted and not much clear
it cant bypass , thats the thing.
