    // Search bar
    var submitButton = document.getElementById("submitButton");
    var textField = document.getElementById("textField");

    textField.onkeyup = function(){
        if (textField.value == "") {
            submitButton.disabled = true;
        } else {
            submitButton.disabled = false;
        }
    }