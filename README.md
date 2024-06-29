# Итоговая аттестация

## Краткое описание задания

Используя фреймворк Django создайте сайт, на котором пользователи смогут добавлять свои рецепты блюд и просматривать рецепты других пользователей.
Готовый проект необходимо сдать в виде ссылки на рабочий сайт в сети интернет и репозитория с исходным кодом проекта.

## Подробное описание задания

### Модели

Для работы с пользователями используйте встроенного в Django User`a.
Подготовьте нижеперечисленные модели:
- Рецепты:
  - Название
  - Описание
  - Шаги приготовления
  - Время приготовления
  - Изображение
  - Автор
  - *другие поля на ваш выбор, например ингредиенты и т.п.
  
- *Категории рецептов
  - Название
  - *другие поля на ваш выбор

- *Связующая таблица для связи Рецептов и Категории
  - *обязательные для связи поля
  - *другие поля на ваш выбор

### Шаблоны

Подготовьте базовый шаблон проекта и нижеперечисленные дочерние шаблоны:
- Главная с 5 случайными рецептами кратко
- Страница с одним подробным рецептом
- Страницы регистрации, авторизации и выхода пользователя
- Страница добавления/редактирования рецепта
- *другие шаблоны на ваш выбор
