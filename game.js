// ウィンドウが完全に読み込まれた後に処理を実行
window.onload = function() {
    const clickButton = document.getElementById("clickButton");
    const resultDisplay = document.getElementById("result");
    const timerDisplay = document.getElementById("timer");
    let clickCount = 0;
    let setTime = 30;
    let timer;

    // ボタンを表示
    clickButton.style.display = "block";

    // ボタンクリック時の処理
    clickButton.addEventListener("click", function() {
        // 最初のクリック時にゲームを開始する
        if (clickCount === 0) {
            startGame();
        }
        if (setTime > 0) { // ゲームが終了していない場合にのみクリック処理を実行
             Math.floor(Math.random());
             Math.floor(Math.random());
            addEmoji();
            playSound();
        }
    });

    // ゲームの開始
    function startGame() {
        resultDisplay.textContent = "Score: 0";
        updateTimerDisplay();
        timer = setInterval(updateTime, 1000); // 1秒ごとに時間を更新
    }

    // ゲーム終了時の処理
    function endGame() {
        clearInterval(timer);
        resultDisplay.textContent = "Game Over! Score: " + clickCount;
        resultDisplay.style.display = "block"; // 結果表示を中央に表示するためにブロック要素に変更
        resultDisplay.style.margin = "auto"; // 結果表示を中央に配置
        // ゲーム終了後にクリックイベントを削除
        clickButton.removeEventListener("click", clickButtonHandler);
    }


    // 残り時間を更新する関数
    function updateTime() {
        setTime--;
        updateTimerDisplay();
        if (setTime === 0) {
            endGame();
        }
    }

    // タイマーの表示を更新する関数
    function updateTimerDisplay() {
        timerDisplay.textContent = setTime;
    }

    // 絵文字の配列
    const emojis = ["😀", "😍", "😎", "🥳", "🤩", "😂", "🤣", "😜", "🤪", "😇"];

    function addEmoji() {
        const emojiContainer = document.getElementById("emoji-container");
        const randomIndex = Math.floor(Math.random() * emojis.length);
        const randomEmoji = emojis[randomIndex];
        const emojiElement = document.createElement("div");
        emojiElement.classList.add("emoji");
        emojiElement.textContent = randomEmoji;
        emojiContainer.appendChild(emojiElement);
        clickCount++;
        resultDisplay.textContent = "Score: " + clickCount;
    }

    // サウンドを再生する関数
       function playSound() {
        audio.play();
    }
};
