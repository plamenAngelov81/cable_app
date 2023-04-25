window.addEventListener("load", create_cable);

function create_cable() {
    const new_cable_create_btn = Array.from(document.getElementsByClassName('create_cable_link'))[0]
    new_cable_create_btn.addEventListener('click', show_cable_create_form)
    const create_form_element = document.getElementById('create_form')
    const create_form_btn = Array.from(create_form_element.children)[6]
    const nameElement = document.getElementById('id_cable_name')
    const capNumberElement = document.getElementById('id_cap_number')
    const clutchNumberElement = document.getElementById('id_clutch_number')
    const inductorTypeElement = document.getElementById('id_inductor_type')
    const machineElement = document.getElementById('id_machine')

    function show_cable_create_form() {
        create_form_element.style.display = 'block'
        new_cable_create_btn.style.display = 'none'
        create_form_btn.addEventListener("click", create_hide)
        nameElement.value = ''
        capNumberElement.value = ''
        clutchNumberElement.value = ''
        inductorTypeElement.value = ''
        machineElement.value = ''
    }

    function create_hide() {
        create_form_element.style.display = 'none'
        new_cable_create_btn.style.display = 'block'
    }
}