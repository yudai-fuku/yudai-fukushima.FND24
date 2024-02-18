'use strict'
// 1行目に記載している 'use strict' は削除しないでください

const startDate = new Date("2016/4/1 0:00:00");// 開始日時
// タイマーを更新する関数
const updateTimer = () => {
    const now = new Date();// 現在日時
    let diff = now.getTime() - startDate.getTime();// 残り時間（ミリ秒）
    // 残り時間から経過日数、時間、分、秒を計算
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((diff / (1000 * 60)) % 60);
    const seconds = Math.floor((diff / 1000) % 60);
    const timerText = `${days}日 ${hours.toString().padStart(2, "0")}:${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;// タイマーを更新
    document.getElementById("timer").textContent = timerText;
    setTimeout(updateTimer, 10);// 10ミリ秒後に再度タイマーを更新する
};
updateTimer();// タイマーを開始

