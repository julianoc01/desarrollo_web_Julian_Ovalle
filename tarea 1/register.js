const validateName = (name) => {
    if(!name) return false;
    let lengthValid = name.trim().length >= 4;
    return lengthValid;
}
const validatePhoneNumber = (phoneNumber) => {
    if (!phoneNumber) return false;
    // validación de longitud
    let lengthValid = phoneNumber.length >= 8;

    // validación de formato
    let re = /^[0-9]+$/;
    let formatValid = re.test(phoneNumber);

    // devolvemos la lógica AND de las validaciones.
    return lengthValid && formatValid;
};
const validateEmail = (email) => {
    if (!email) return false;
    let lengthValid = email.length > 15;

    // validamos el formato
    let re = /^[\w.]+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
    let formatValid = re.test(email);

    // devolvemos la lógica AND de las validaciones.
    return lengthValid && formatValid;
};
const validateSelect = (select) => {
    if(!select) return false;
    return true
}
const validateComuna = (comuna) => {
    if(!comuna) return false;
    let lengthValid = comuna.trim().length >= 4;
    return lengthValid;
}
const validateContrasena = ( contasena,contasena2) => {
    if (contasena.length < 4 || contasena2.length< 4) return false
    if (!contasena || !contasena2) return false;
    if (contasena != contasena2) return false;
    return true
}


const validarForm = () => {
    let nombreinput = document.getElementById("nombre")
    let telefonoinput = document.getElementById("telefono")
    let correoinput = document.getElementById("mail")
    let regioninput = document.getElementById("region")
    let comunainput = document.getElementById("comuna")
    let contrasena1input = document.getElementById("contraseña")
    let contrasena2input = document.getElementById("contraseña2")

    let msg = ""
    let valid = false

    if (!validateName(nombreinput.value)) {
        msg += "Nombre invalido!\n";
        nombreinput.style.borderColor = "red"; // cambiar estilo con JS!!
    } else {
        nombreinput.style.borderColor = "";
    }

    if (!validatePhoneNumber(telefonoinput.value)) {
        msg += "Telefono invalido!\n";
        telefonoinput.style.borderColor = "red";
    } else {
        telefonoinput.style.borderColor = "";
    }

    if (!validateEmail(correoinput.value)) {
        msg += "Correo electronico invalido!\n";
        correoinput.style.borderColor = "red";
    } else {
        correoinput.style.borderColor = "";
    }

    if (!validateSelect(regioninput.value)) {
        msg += "region invalida!\n";
        regioninput.style.borderColor = "red";
    } else {
        regioninput.style.borderColor = "";
    }
    if(!validateComuna(comunainput.value)){
        msg += "comuna invalida";
        comunainput.style.borderColor = "red"
    } else{
        comunainput.style.borderColor = ""
    }
    if (!validateContrasena(contrasena1input.value,contrasena2input.value)){
        msg += "Contraseña muy debil o no coinciden"
        contrasena1input.style.borderColor = "red"
        contrasena2input.style.borderColor= "red"
    } else{
        contrasena1input.style.borderColor = ""
        contrasena2input.style.borderColor= ""
    }

    if (msg === "") {
        msg = "Cuenta creada exitosamente!";
        valid = true
        let username = nombreinput.value;
        localStorage.setItem("username", username);
    }
    alert(msg);
    if (valid) {
        window.location.href = "panel.html";
    }
}








let submitBtn = document.getElementById("envio");
submitBtn.addEventListener("click", validarForm);
