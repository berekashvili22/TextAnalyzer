function myFunction() {
    var mainFrameOne = document.getElementById("mainFrameOne"); 
    var mainFrameTwo = document.getElementById("mainFrameTwo");

    var elem = document.getElementById("myButton1");

    if (elem.innerText=="შეიყვანე ტექსტი") elem.innerText = "ატვირთე ფაილი";
    else elem.innerText = "შეიყვანე ტექსტი";
 
    mainFrameOne.style.display = (
        mainFrameOne.style.display == "none" ? "block" : "none"); 
    mainFrameTwo.style.display = (
        mainFrameTwo.style.display == "none" ? "block" : "none"); 
 }