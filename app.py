import streamlit as st

st.title("Formulario de registro estudiantil")

nombre = st.text_input("Nombre Completo")
edad = st.number_input("Edad", min_value=0, max_value=80, step=1)
carrera = st.selectbox("Carrera", ["Seleccione una opcion", "Ingenieria en computacion", "Diseno Web", "Tecnico en informatica"])
correo = st.text_input("Correo electronico")
telefono = st.text_input("Numero de telefono")
comentario = st.text_area("Comentario adicional (opcional)")

if st.button("Enviar"):

    if nombre == "":
        st.warning("Debe ingresar el nombre completo")

    elif edad == 0:
        st.warning("Debe ingresar una edad valida")

    elif carrera == "Seleccione una opcion":
        st.warning("Debe seleccionar una carrera")

    elif correo == "":
        st.warning("Debe ingresar un correo electronico")

    elif telefono == "":
        st.warning("Debe ingresar un numero de telefono")

    else:
        st.write("#### Datos ingresados:")
        st.write(f"Nombre: {nombre}")
        st.write(f"Edad: {edad}")
        st.write(f"Carrera: {carrera}")
        st.write(f"Correo: {correo}")
        st.write(f"Telefono: {telefono}")

        if comentario != "":
            st.write(f"Comentario: {comentario}")

        st.success("Formulario enviado con exito")
