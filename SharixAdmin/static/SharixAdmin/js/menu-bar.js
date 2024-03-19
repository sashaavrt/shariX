// Получаем элементы из DOM
const menuBarEl = document.getElementById('menu-bar'); // Элемент меню
const menuBarImgArrowEl = document.getElementById('menu-bar-img-arrow'); // Элемент стрелки в меню
const menuBarLabelEls = document.querySelectorAll('.menu-bar-label'); // Коллекция элементов меток в меню
const userWorkspaceEl = document.getElementById('user-workspace'); // Элемент рабочей области пользователя

// Проверяем, открыто ли меню, и устанавливаем значение по умолчанию, если в localStorage нет информации
if (localStorage.getItem('menuBarOpened') === null) localStorage.setItem('menuBarOpened', true);

// Функция для управления видимостью меню
function menuBarControll() {
    // Получаем значение открытия меню из localStorage
    let menuBarOpened = localStorage.getItem('menuBarOpened');
    let menuBarWidth;

    // Устанавливаем ширину меню в зависимости от его состояния (открыто/закрыто)
    if (menuBarOpened === 'true') {
        // Ширина меню при закрытом состоянии
        menuBarWidth = 74; 
        // Устанавливаем нулевую прозрачность для каждой метки в меню
        menuBarLabelEls.forEach(function(el) { el.style.opacity = 0; });
        // Поворачиваем стрелку на 0 градусов
        menuBarImgArrowEl.style.transform = 'rotate(0deg)';
    } else {
        // Ширина меню при октрытом состоянии
        menuBarWidth = 280;
        // Устанавливаем полную прозрачность для каждой метки в меню
        menuBarLabelEls.forEach(function(el) { el.style.opacity = 1; });
        // Поворачиваем стрелку на 180 градусов
        menuBarImgArrowEl.style.transform = 'rotate(180deg)';
    }

    // Устанавливаем необходимую ширину меню и отступ рабочей области пользователя
    menuBarEl.style.minWidth = menuBarWidth + 'px';
    userWorkspaceEl.style.marginLeft = menuBarWidth + 16 + 'px';
}

// Функция для переключения состояния открытия меню
function menuBarSwitch() {
    // Получаем текущее значение открытия меню из localStorage
    let menuBarOpened = localStorage.getItem('menuBarOpened');
    // Инвертируем значение (true -> false, false -> true)
    menuBarOpened = menuBarOpened === 'true' ? false : true;
    // Сохраняем новое значение в localStorage
    localStorage.setItem('menuBarOpened', menuBarOpened);
    // Вызываем функцию управления меню для обновления его внешнего вида
    menuBarControll();
}
