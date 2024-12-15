const images_cards = [
    '1.1_ace_hearts.png',
    '1.2_two_hearts.png',
    '1.3_three_hearts.png',
    '1.4_four_hearts.png',
    '1.5_five_hearts.png',
    '1.6_six_hearts.png',
    '1.7_seven_hearts.png',
    '1.8_eight_hearts.png',
    '1.9_nine_hearts.png',
    '1.10_ten_hearts.png',
    '1.11_jack_hearts.png',
    '1.12_queen_hearts.png',
    '1.13_king_hearts.png',
    '2.1_ace_clubs.png',
    '2.2_two_clubs.png',
    '2.3_three_clubs.png',
    '2.4_four_clubs.png',
    '2.5_five_clubs.png',
    '2.6_six_clubs.png',
    '2.7_seven_clubs.png',
    '2.8_eight_clubs.png',
    '2.9_nine_clubs.png',
    '2.10_ten_clubs.png',
    '2.11_jack_clubs.png',
    '2.12_queen_clubs.png',
    '2.13_king_clubs.png',
    '3.1_ace_diamonds.png',
    '3.2_two_diamonds.png',
    '3.3_three_diamonds.png',
    '3.4_four_diamonds.png',
    '3.5_five_diamonds.png',
    '3.6_six_diamonds.png',
    '3.7_seven_diamonds.png',
    '3.8_eight_diamonds.png',
    '3.9_nine_diamonds.png',
    '3.10_ten_diamonds.png',
    '3.11_jack_diamonds.png',
    '3.12_queen_diamonds.png',
    '3.13_king_diamonds.png',
    '4.1_ace_spades.png',
    '4.2_two_spades.png',
    '4.3_three_spades.png',
    '4.4_four_spades.png',
    '4.5_five_spades.png',
    '4.6_six_spades.png',
    '4.7_seven_spades.png',
    '4.8_eight_spades.png',
    '4.9_nine_spades.png',
    '4.10_ten_spades.png',
    '4.11_jack_spades.png',
    '4.12_queen_spades.png',
    '4.13_king_spades.png',
];
// Функция для получения случайных карт
function getRandomCards(arr, num) {
    const randomIndexes = new Set(); // Используем Set для уникальности индексов

    // Генерируем уникальные случайные индексы
    while (randomIndexes.size < num) {
        const randomIndex = Math.floor(Math.random() * arr.length); // Генерируем случайный индекс
        randomIndexes.add(randomIndex); // Добавляем индекс в Set (игнорирует дубликаты)
    }

    // Получаем карты по случайным индексам
    return Array.from(randomIndexes).map(index => arr[index]); // Преобразуем Set в массив и выбираем карты
}

// Получаем 5 случайных карт из массива
const randomCards = getRandomCards(images_cards, 5); // Исправлено на images_cards

// Получаем контейнер для карт из HTML 
const container = document.getElementById('image-card-container');

// Проверяем, существует ли контейнер
if (container) {
    // Для каждой случайной карты создаем элемент img и добавляем его в контейнер
    randomCards.forEach(card => {
        const imgElement = document.createElement('img'); // Создаем новый элемент img
        imgElement.src = 'img/cards/' + card; // Устанавливаем путь к изображению карты
        imgElement.alt = card; // Устанавливаем альтернативный текст
        container.appendChild(imgElement); // Добавляем элемент img в контейнер
    });
} else {
    console.error('Контейнер для карт не найден!');
}
