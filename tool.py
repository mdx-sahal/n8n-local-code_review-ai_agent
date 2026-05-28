from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import re

app = FastAPI(title="Agent Code Reader Tool")
SAFE_DIRECTORY = Path(__file__).parent.resolve()

class ChatPayload(BaseModel):
    # This captures the raw chat interaction dictionary sent from n8n
    action: dict = {}

@app.get("/list-files")
def list_files():
    """Lists files in the target project directory."""
    try:
        files = [f.name for f in SAFE_DIRECTORY.iterdir() if f.is_file()]
        return {"directory": str(SAFE_DIRECTORY), "files": files}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/read-file")
def read_file(payload: ChatPayload):
    """Fallback-safe text scanner to find and read the file content."""
    try:
        # Pull the absolute raw text string typed by the user in chat
        user_message = payload.action.get("chatInput", "")
        
        # Simple Regex fallback: Look for filenames like 'tool.py', 'main.py', etc.
        match = re.search(r'([\w-]+\.(?:py|js|json|txt|md|html|css))', user_message, re.IGNORECASE)
        
        if not match:
            raise HTTPException(status_code=400, detail="Could not extract a filename from the chat input context.")
            
        filename = match.group(1)
        safe_path = SAFE_DIRECTORY / filename
        
        if not safe_path.exists():
            raise HTTPException(status_code=404, detail=f"File '{filename}' not found in directory.")
            
        return {"filename": filename, "content": safe_path.read_text(encoding="utf-8")}
        
    except Exception as e:
        if isinstance(e, HTTPException): raise e
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)