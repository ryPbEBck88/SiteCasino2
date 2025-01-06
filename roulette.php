<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Рулетка</title>
    <style>
        #roulette-container {
            width: 300px;
            height: 300px;
            border-radius: 50%;
            position: relative;
            overflow: hidden;
            border: 2px solid #333;
            margin: 20px auto;
        }
        .segment {
            position: absolute;
            width: 0;
            height: 0;
            border-left: 150px solid transparent;
            border-right: 150px solid transparent;
            border-bottom: 300px solid;
            transform-origin: 150px 150px;
        }
        button {
            display: block;
            margin: 20px auto;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }
        #result {
            text-align: center;
            font-size: 20px;
        }
    </style>
</head>
<body>
    <div id="roulette-container">
        <?php
            $segments = ["Победа!", "Попытайся еще", "Приз!", "Удача", "Бонус", "Подарок"];
            $segmentCount = count($segments);
            $angleStep = 360 / $segmentCount;

            for ($i = 0; $i < $segmentCount; $i++) {
                $angle = $i * $angleStep;
                $color = sprintf('#%06X', mt_rand(0, 0xFFFFFF)); // Случайный цвет
                echo "<div class='segment' style='transform: rotate({$angle}deg); border-bottom-color: {$color};'></div>";
            }
        ?>
    </div>
    <button id="spin-button">Крутить!</button>
    <div id="result"></div>

    <script>
        const spinButton = document.getElementById('spin-button');
        const rouletteContainer = document.getElementById('roulette-container');
        const resultDiv = document.getElementById('result');
        const segments = <?php echo json_encode($segments); ?>;
        const segmentCount = segments.length;
        let isSpinning = false;

        spinButton.addEventListener('click', () => {
            if (isSpinning) return;
            isSpinning = true;
            resultDiv.textContent = '';

            const randomSpin = Math.floor(Math.random() * 360 * 5) + 720; // Спины + случайный угол
            const finalAngle = randomSpin % 360;

            rouletteContainer.style.transition = 'transform 4s cubic-bezier(0.25, 0.8, 0.25, 1)';
            rouletteContainer.style.transform = `rotate(${randomSpin}deg)`;

            setTimeout(() => {
                rouletteContainer.style.transition = '';
                rouletteContainer.style.transform = 'rotate(0deg)';
                isSpinning = false;

                let winningIndex = Math.floor((360 - finalAngle) / (360 / segmentCount));
                winningIndex = winningIndex === segmentCount ? 0 : winningIndex;

                resultDiv.textContent = `Вы выиграли: ${segments[winningIndex]}`;

            }, 4100); // Задержка чуть больше анимации
        });
    </script>
</body>
</html>