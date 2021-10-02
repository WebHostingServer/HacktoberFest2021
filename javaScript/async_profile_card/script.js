"use strict";

let profile = document.getElementById('profile')    //  profile change button
let profilepicture = document.getElementById('profilepicture')  //  profile card 
console.log(profilepicture)


//  adding an onchange listener to the change file button
profile.addEventListener('change', (e) => {
    let files = e.target.files;     //  getting the file information whenever a new change happens
    if(files && files[0]) {
        let reader = new FileReader();  //  creating a file reader instance 
        reader.onload = () => {
            profilepicture.setAttribute('src', reader.result)   //  setting the source for the new image
        }

        reader.readAsDataURL(files[0]);
    } else {
        window.alert('Choose a correct file')
    }
})