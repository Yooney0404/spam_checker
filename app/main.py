from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.spam import check_spam

# FastAPI 앱 생성 및 설정
app = FastAPI(title="SpamCheck Web")

# 정적 HTML 파일 서빙 설정 (/static 경로로 접근 가능)
app.mount("/static", StaticFiles(directory="static"), name="static")

# 메인 페이지 (/) 접속 시 index.html 반환
@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

# 스팸 분류 요청 처리 (/classify)
@app.post("/classify")
async def classify(request: Request):
    payload = await request.json()
    text = payload.get("text", "")
    label, score = check_spam(text)
    return {"label": label, "score": score}