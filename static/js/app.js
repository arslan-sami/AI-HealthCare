const chatButton = document.querySelector('.chatbox__button');
const chatContent = document.querySelector('.chatbox__support');
const icons = {
    // isClicked: '<img src="{% static 'img/icons/chatbox.png' %}" >',
    // isNotClicked: '<img src="{% static 'img/icons/chatbox.png' %}" >'
}
const chatbox = new InteractiveChatbox(chatButton, chatContent, icons);
chatbox.display();
chatbox.toggleIcon(false, chatButton);


// function prescription() {
//     date = Date.now;
//     document.getElementById('id_modalbody').innerHTML += "<p id='id_date'>12</p> <button class='btn btn-primary w-25'>See Prescription</button>" ;
// }
// function validateForm() {
//     let name = document.forms["appointmentform"]["Your_Name"].value;
//     let age = document.forms['appointmentform']['Age'].value;
//     let disease = document.forms['appointmentform']['Disease'].value;
//     let doctor_selection = document.forms['appointmentform']['Doctor'].value;
//     if (name == "" && name.length >= 3) {
//       prompt("Name must be filled out");
//       return false;
//     }
//     else if (disease == ''){
//         alert("Disease must be filled out");
//         return false;
//     }
//     else if (age == '' && age == String){
//         alert("Enter Your Age must be filled out");
//         return false;
//     }
//     else if (doctor_selection.Select = none){
//         alert("Select the Doctor Must");
//         return false;
//     }
//   }