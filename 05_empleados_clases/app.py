import empleados_services as ep
import streamlit as st

empresa = ep.Empresa("empleados.csv")

tab_nuevo, tab_buscar = st.tabs(["Nuevo Empleado", "Buscar Empleado"])

with tab_nuevo:
    st.subheader("Alta de empleados")
    name = st.text_input("Nombre: ")
    age = st.number_input("Edad: ")
    salary = st.number_input("Salario: ")
    departament = st.text_input("Departamento: ")
    
    if st.button("Guardar"):
        empleado = ep.Empleado(name, age, salary, departament)
        empresa.alta_empleado(empleado)
        st.toast("Empleado Añadido!")

with tab_buscar:
    st.subheader("Busqueda de empleados")
    name= st.text_input("Nombre: ", key="fnombre")
    if st.button("Buscar"):
        empleado=empresa.buscar_empleado(name)
        if empleado!=None:
            st.write(f"Nombre: {empleado.name}")
            st.write(f"Edad: {empleado.age}")
            st.write(f"Salario: {empleado.salary}")
            st.write(f"Departamento: {empleado.departament}")
        else:
            st.toast("Empleado no existente!!")
            
with tab_buscar:
    st.subheader("Busqueda de empleados")
    name= st.text_input("Nombre: ", key="fnombre")
    if st.button("Buscar"):
        empleado=empresa.buscar_empleado(name)
        if empleado!=None:
            st.write(f"Nombre: {empleado.name}")
            st.write(f"Edad: {empleado.age}")
            st.write(f"Salario: {empleado.salary}")
            st.write(f"Departamento: {empleado.departament}")
        else:
            st.toast("Empleado no existente!!")
            

            
            
            



    