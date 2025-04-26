from flask import Flask, request, render_template
import requests
import time

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    # Get form fields
    business_type = request.form.get("business_type", "")
    state = request.form.get("state", "")
    business_structure = request.form.get("business_structure", "")
    initial_prompt = request.form.get("prompt") or ""
    follow_up = request.form.get("follow_up") or ""
    history = request.form.get("conversation_history") or ""

    # Build user message
    if not history:
        history = (
            f"User:\n"
            f"Business Type: {business_type}\n"
            f"State: {state}\n"
            f"Structure: {business_structure}\n"
            f"Initial Request: {initial_prompt.strip()}"
        )

    if follow_up:
        history += f"\n\nUser: {follow_up.strip()}"

    # Build final prompt for LLM (simulated chat)
    full_prompt = (
        "You are a world-class business startup consultant.\n\n"
        "Use the following conversation to guide the user. Provide clear, helpful answers about licensing, "
        "state requirements, tax registration, and forming their business. Include EIN instructions and state-specific info.\n\n"
        f"{history}\n\nAssistant:"
    )

    # Send to Ollama
    try:
        start = time.time()
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2:latest",  # Or llama2, mistral, etc.
                "prompt": full_prompt,
                "temperature": 0.5,
                "num_predict": 1000,
                "stream": False
            }
        )
        elapsed = round(time.time() - start, 2)
        data = response.json()
        assistant_reply = data.get("response", "⚠️ No response received.")
    except Exception as e:
        assistant_reply = f"⚠️ Error contacting model: {e}"
        elapsed = None

    # Update conversation
    history += f"\n\nAssistant: {assistant_reply.strip()}"

    return render_template("index.html",
                           response=assistant_reply,
                           business_type=business_type,
                           state=state,
                           business_structure=business_structure,
                           conversation_history=history)
