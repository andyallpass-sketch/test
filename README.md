# Test Project

這是一個使用 `uv` 進行套件與虛擬環境管理的 Python 專案。

## 環境建置

1. 確保系統中已安裝 `uv` (若無，可執行 `pip install uv` 或參考 [官方文件](https://github.com/astral-sh/uv))。
2. 啟動虛擬環境：
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`

## 安裝依賴

進入虛擬環境後，您可以使用 `uv` 來極速安裝套件：

```bash
uv pip install <package_name>
```

若有 `requirements.txt`：

```bash
uv pip install -r requirements.txt
```

## 開發工具設定 (pre-commit)

本專案使用 `pre-commit` 來確保程式碼品質與風格一致性。主要使用了 `ruff` 作為 Linter 與 Formatter。

### 安裝 pre-commit

在虛擬環境中執行以下指令來安裝 `pre-commit`：

```bash
uv pip install pre-commit
```

### 安裝 Git Hook

安裝套件後，請執行以下指令將 `pre-commit` 綁定到 Git 的 commit 流程中：

```bash
pre-commit install
```

這樣一來，每次執行 `git commit` 時，系統都會自動檢查程式碼排版與潛在錯誤。若想手動執行檢查所有檔案，可以使用：

```bash
pre-commit run --all-files
```
