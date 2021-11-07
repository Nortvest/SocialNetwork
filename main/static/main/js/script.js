const form_elements = document.forms.reg

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

for (el of form_elements){
    if (el.name !== 'password1' && el.name !== 'password2'){
        el.addEventListener('blur', function (e){
            let el_id = e.target.id
            if (e.target.value){
                let data = {
                    csrfmiddlewaretoken: getCookie('csrftoken'),
                    [e.target.name]: e.target.value
                }
    
                $.ajax({
                    type: 'POST',
                    url: 'validation_of_login_or_registration',
                    data: data,
                    success: function(d) {
                        if (d['success']){
                            document.querySelector('#' + el_id + '_errors').innerHTML = ''
                            document.querySelector('#' + el_id).classList.remove('is-invalid')
                            document.querySelector('#' + el_id).classList.add('is-valid')
                        } else {
                            document.querySelector('#' + el_id).classList.remove('is-valid')
                            document.querySelector('#' + el_id).classList.add('is-invalid')
                            document.querySelector('#' + el_id + '_errors').innerHTML = d['text']
                        }
                    }
                });
            } else {
                document.querySelector('#' + el_id + '_errors').innerHTML = ''
                document.querySelector('#' + el_id).classList.remove('is-invalid')
                document.querySelector('#' + el_id).classList.remove('is-valid')
            }
        })
    }
}


document.getElementById('id_password1').addEventListener('blur', function (e){
    if (document.querySelector('#id_password1').value && document.querySelector('#id_password2').value){
        let data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            password1: document.querySelector('#id_password1').value,
            password2: document.querySelector('#id_password2').value
        }

        $.ajax({
            type: 'POST',
            url: 'validation_of_login_or_registration',
            data: data,
            success: function(d) {
                if (d['success']){
                    document.querySelector('#id_password2_errors').innerHTML = ''
                    document.querySelector('#id_password1').classList.remove('is-invalid')
                    document.querySelector('#id_password1').classList.add('is-valid')
                    document.querySelector('#id_password2').classList.remove('is-invalid')
                    document.querySelector('#id_password2').classList.add('is-valid')
                } else {
                    document.querySelector('#id_password1').classList.remove('is-valid')
                    document.querySelector('#id_password1').classList.add('is-invalid')
                    document.querySelector('#id_password2').classList.remove('is-valid')
                    document.querySelector('#id_password2').classList.add('is-invalid')
                    document.querySelector('#id_password2_errors').innerHTML = d['text']
                }
            }
        });
    } else {
        document.querySelector('#id_password2_errors').innerHTML = ''
        document.querySelector('#id_password1').classList.remove('is-invalid')
        document.querySelector('#id_password1').classList.remove('is-valid')
        document.querySelector('#id_password2').classList.remove('is-invalid')
        document.querySelector('#id_password2').classList.remove('is-valid')
    }
})

document.getElementById('id_password2').addEventListener('blur', function (e){
    if (document.querySelector('#id_password1').value && document.querySelector('#id_password2').value){
        let data = {
            csrfmiddlewaretoken: getCookie('csrftoken'),
            password1: document.querySelector('#id_password1').value,
            password2: document.querySelector('#id_password2').value
        }

        $.ajax({
            type: 'POST',
            url: 'validation_of_login_or_registration',
            data: data,
            success: function(d) {
                if (d['success']){
                    document.querySelector('#id_password2_errors').innerHTML = ''
                    document.querySelector('#id_password1').classList.remove('is-invalid')
                    document.querySelector('#id_password1').classList.add('is-valid')
                    document.querySelector('#id_password2').classList.remove('is-invalid')
                    document.querySelector('#id_password2').classList.add('is-valid')
                } else {
                    document.querySelector('#id_password1').classList.remove('is-valid')
                    document.querySelector('#id_password1').classList.add('is-invalid')
                    document.querySelector('#id_password2').classList.remove('is-valid')
                    document.querySelector('#id_password2').classList.add('is-invalid')
                    document.querySelector('#id_password2_errors').innerHTML = d['text']
                }
            }
        });
    } else {
        document.querySelector('#id_password2_errors').innerHTML = ''
        document.querySelector('#id_password1').classList.remove('is-invalid')
        document.querySelector('#id_password1').classList.remove('is-valid')
        document.querySelector('#id_password2').classList.remove('is-invalid')
        document.querySelector('#id_password2').classList.remove('is-valid')
    }
})
