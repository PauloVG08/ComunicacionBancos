document.addEventListener("DOMContentLoaded", function () {
  console.log("cargando");
  let url = "http://127.0.0.1:8080/obtenerBancos";

  fetch(url)
    .then((response) => {
      return response.json();
    })
    .then(function (data) {
      console.log("datos" + data);

      if (data == "") {
        Swal.fire(
          "",
          "Error interno del Servidor, por favor vuelve a intentarlo.",
          "error"
        );
        return;
      }

      if (data.result.exception != null) {
        Swal.fire(
          "",
          "Error interno del servidor. Intente nuevamente mas tarde.",
          "error"
        );
        return;
      }
      if (data.result.error != null) {
        Swal.fire("", data.error, "warning");
        return;
      }
      importarBancos(data.result);
    })
    .catch((error) => {
      Swal.fire(
        "",
        "Error interno del servidor al obtener los bancos. Intente nuevamente mas tarde.",
        "error"
      );
    });
});

function importarBancos(data) {
  let selectBancos = document.getElementById("bancoSelected");
  //poner su banco correspondiente
  let content = "<option value='banamex'>BANAMEX</option>";
  bancos = data;

  bancos.forEach(function (banco) {
    let dato =
      "<option value='" +
      banco.nombre_banco +
      "'>" +
      banco.nombre_banco +
      "</option>";
    content += dato;
  });

  selectBancos.innerHTML = content;
}

function validarDatos() {
  let cuenta = document.getElementById("txtNumeroTarjeta").value;
  let nip = document.getElementById("txtNip").value;
  let monto = document.getElementById("txtMonto").value;
  let valido = true;

  console.log(cuenta.length);

  try {
    // Asegurarse de que 'Número de Cuenta' es una cadena y no 'undefined' o null
    if (typeof cuenta !== "string") {
      throw new Error("El Número de Cuenta debe ser numerico");
    }

    let cuentaInt = parseInt(cuenta, 10); // Añadir la base (10) para parseo seguro

    // Añadir una validación para comprobar si el resultado es un número
    if (isNaN(cuentaInt)) {
      throw new Error("El Número de Cuenta debe ser numerico");
    }

    // Opcional: Añadir una validación para comprobar la longitud del Número de Cuenta
    if (cuenta.length !== 4) {
      throw new Error("Ingrese su Número de Cuenta a 4 digitos");
    }

    document.getElementById("lblValidarNip").style.display = "none";
    console.log("cuenta " + cuentaInt);
  } catch (error) {
    // Mejorar el manejo de errores para ser más específico
    document.getElementById("lblValidarCuenta").innerText = error.message;
    document.getElementById("lblValidarCuenta").style.display = "block";
    valido = false;
  }

  try {
    // Asegurarse de que 'nip' es una cadena y no 'undefined' o null
    if (typeof nip !== "string") {
      throw new Error("El NIP debe ser numerico");
    }

    let nipInt = parseInt(nip, 10); // Añadir la base (10) para parseo seguro

    // Añadir una validación para comprobar si el resultado es un número
    if (isNaN(nipInt)) {
      throw new Error("El NIP debe ser numerico");
    }

    // Opcional: Añadir una validación para comprobar la longitud del NIP
    if (nip.length !== 4) {
      throw new Error("Ingrese su NIP a 4 digitos");
    }

    document.getElementById("lblValidarNip").style.display = "none";
    console.log("cuenta " + nipInt);
  } catch (error) {
    // Mejorar el manejo de errores para ser más específico
    document.getElementById("lblValidarNip").innerText = error.message;
    document.getElementById("lblValidarNip").style.display = "block";
    valido = false;
  }

  try {
    // Asegurarse de que 'monto' es una cadena y no 'undefined' o null
    if (typeof monto !== "string") {
      throw new Error("El monto debe ser un valor numérico");
    }

    let montoFloat = parseFloat(monto); // Parsear como float

    // Validar si el resultado es un número
    if (isNaN(montoFloat)) {
      throw new Error("El monto debe ser un valor numérico");
    }

    // que no tenga más de dos decimales
    if (!/^(\d+(\.\d{0,2})?)$/.test(monto)) {
      throw new Error("El monto no puede tener más de dos decimales");
    }

    console.log("Monto: " + montoFloat);
    document.getElementById("lblValidarMonto").style.display = "none";
  } catch (error) {
    // Manejo de errores
    document.getElementById("lblValidarMonto").innerText = error.message;
    document.getElementById("lblValidarMonto").style.display = "block";
    valido = false;
  }

  if (valido) {
    limpiarValidaciones();
  }

  return valido;
}

function limpiarValidaciones() {
  document.getElementById("lblValidarCuenta").style.display = "none";
  document.getElementById("lblValidarNip").style.display = "none";
  document.getElementById("lblValidarMonto").style.display = "none";
}

function limpiarCampos() {
  document.getElementById("txtNumeroTarjeta").value = "";
  document.getElementById("txtNip").value = "";
  document.getElementById("txtMonto").value = "";
  document.getElementById("bancoSelected").value = "banamex";
}

function realizarRetiro() {
  if (validarDatos()) {
    let banco = document.getElementById("bancoSelected").value;
    let cuenta = document.getElementById("txtNumeroTarjeta").value;
    let nip = document.getElementById("txtNip").value;
    let monto = document.getElementById("txtMonto").value;

    if (banco != "banamex") {
      console.log("se selecciono un banco externo");

      const url =
        "http://127.0.0.1:8080/retirarExterno/" +
        cuenta +
        "/" +
        nip +
        "/" +
        monto +
        "/" +
        banco;

      const data = {
        cuenta,
        nip,
        monto,
        banco,
      };

      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          if (data == null) {
            Swal.fire(
              "",
              "Error interno del Servidor, por favor vuelve a intentarlo.",
              "error"
            );
            return;
          }

          if (data.result.exception != null) {
            Swal.fire(
              "",
              "Error interno del servidor. Intente nuevamente mas tarde.",
              "error"
            );
            return;
          }

          if (data.result.error != null) {
            Swal.fire("", data.result.error, "warning");
            return;
          }

          if (data.result.Error != null) {
            Swal.fire("", data.result.Error, "error");
            return;
          }

          Swal.fire("", "Retiro Realizado con Exito!", "success");
          limpiarValidaciones();
          limpiarCampos();
        });
    } else {
      const url =
        "http://127.0.0.1:8080/retirar/" +
        cuenta +
        "/" +
        nip +
        "/" +
        monto +
        "/0";

      const data = {
        cuenta,
        nip,
        monto,
      };

      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((data) => {
          if (data == null) {
            Swal.fire(
              "",
              "Error interno del Servidor, por favor vuelve a intentarlo.",
              "error"
            );
            return;
          }

          if (data.result.exception != null) {
            Swal.fire(
              "",
              "Error interno del servidor. Intente nuevamente mas tarde.",
              "error"
            );
            return;
          }

          if (data.result.error != null) {
            Swal.fire("", data.error, "warning");
            return;
          }

          if (data.result.Error != null) {
            Swal.fire("", data.result.Error, "error");
            return;
          }

          Swal.fire("", "Retiro Realizado con Exito!", "success");
          limpiarValidaciones();
          limpiarCampos();
        });
    }
  }
}
