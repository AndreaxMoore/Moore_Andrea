/**
 * Created by moorea8957 on 3/30/2017.
 */
function validate(){
    var x = document.forms.input.username.value;
    var y = document.forms.input.password.value;
    var atPos = x.indexOf("@");
    var dotPos = x.lastIndexOf(".");
    //we need...username@webAddress.extension
    //if, then following...
    //@is not in the string
    //@ is in the wrong place
    //there is no .com, .gov. or any other extension
    //final dot is in the wrong place

    

    if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
        //if (y.length < 6 )
            //alert("Both username and password are incorrect")
        if (y.length > 6)
            alert("We were unable to process your request. Please correct the following errors..." +
                "You did not provide a valid email address ");
        else
            alert("Both username and password are incorrect");

    else if(y.length < 6 )
        //if(atPos < 1 || dotPos < atPos+2 || dotPos + 2 > x.length)
            //alert("Both username and password are incorrect");
            alert("We were unable to process your request. Please correct the following errors..." +"" +
            "Your password does not meet the minimum requirements.");
    else
        alert("Success!");
}

