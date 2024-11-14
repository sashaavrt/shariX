// Функция, запрещающая нажатие кнопки отправки формы", пока пользователь поставит галочки в указанные чекбоксы
function makeCheckboxesMandatory(submitBtnEl, ...checkboxEls) {
    checkboxEls.forEach(checkboxEl => {
        checkboxEl.addEventListener('change', function() {
            if (checkboxEls.every(el => el.checked)) submitBtnEl.removeAttribute('disabled');
            else submitBtnEl.setAttribute('disabled', 'disabled');
        });
    });
}