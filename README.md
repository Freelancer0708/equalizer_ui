# 🎧 Equalizer APO Preamp Controller

Windows上で [Equalizer APO](https://sourceforge.net/projects/equalizerapo/) の `Preamp`（全体音量）を簡単に調整できるPython製GUIツールです。  
爆音防止や静音環境の維持に最適です。

---

## ✨ 機能

- スライダーで Preamp（-60 dB ～ -40 dB）を直感的に変更
- `config.txt` を自動書き換え
- PyInstallerで `.exe` 化可能（GUI・黒いウィンドウなし）
- 管理者権限付きショートカット対応

---

## 🛠️ 使い方

### ✅ 1. Equalizer APO をインストール  
👉 https://sourceforge.net/projects/equalizerapo/

インストール時に、使用している再生デバイス（スピーカーやイヤホン）にチェックを入れてください。

---

### ✅ 2. このリポジトリをクローン

```bash
git clone https://github.com/Freelancer0708/equalizer_ui.git
cd equalizer-apo-preamp-controller
```

---

### ✅ 3. Pythonでスクリプトを実行

```bash
python equalizer_ui.py
```

※ .pyw にリネームすると、コンソールが表示されません（GUIのみ）

---

### 📦 .exe化して使う（PyInstaller）
#### 🔧 ① PyInstaller をインストール
```bash
pip install pyinstaller
```

---

#### 🔧 ② .exe を生成（コンソール非表示）
```bash
pyinstaller --onefile --noconsole equalizer_ui.py
```
完了後：
- 実行ファイルは dist/equalizer_ui.exe に出力されます
- この .exe をそのまま起動可能です（インストール不要）

---

#### 🔒 ③ 管理者として実行（必要に応じて）
1. equalizer_ui.exe のショートカットを作成
2. 右クリック → [プロパティ] → [ショートカット] → [詳細設定]
3. ✅ 「管理者として実行」にチェック

---

### 📁 注意点
- config.txt のパス（通常）：
    C:\Program Files\EqualizerAPO\config\config.txt

- 書き換えには 管理者権限が必要な場合があります

---