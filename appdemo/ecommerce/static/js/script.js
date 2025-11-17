const { use } = require("react");

function validateSignup()
{
    const username = document.getElementById('uname');
    const password = document.getElementById('pass');

    const valid_uname = /^\w{10,15}$/;
    const valid_pass = '/^w{8,20}/';
    const valid_email = '/^\w+\@(\w+\.)+\w+$/';
    const valid_num =  '/^\d{10,15}$/';


    if(username.value.trim()==" ")
        username.
}