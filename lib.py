import os

def create_js_ai_library(filename="aiHelper.js"):
    """
    Creates a JavaScript AI helper library file with basic AI fetch functionality.
    """
    # JavaScript library content
    js_code = """\
// aiHelper.js
// Simple AI helper library for JavaScript projects
// Usage: import { askAI } from './aiHelper.js';

export async function askAI(prompt, apiKey) {
    if (!prompt || typeof prompt !== 'string') {
        throw new Error("Prompt must be a non-empty string.");
    }
    if (!apiKey || typeof apiKey !== 'string') {
        throw new Error("API key must be provided as a string.");
    }

    try {
        const response = await fetch("https://api.openai.com/v1/chat/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": `Bearer ${apiKey}`
            },
            body: JSON.stringify({
                model: "gpt-3.5-turbo",
                messages: [{ role: "user", content: prompt }],
                max_tokens: 100
            })
        });

        if (!response.ok) {
            throw new Error(`API request failed with status ${response.status}`);
        }

        const data = await response.json();
        return data.choices?.[0]?.message?.content?.trim() || "";
    } catch (error) {
        console.error("AI request error:", error);
        throw error;
    }
}
"""

    # Write the JS file
    with open(filename, "w", encoding="utf-8") as f:
        f.write(js_code)

    print(f"JavaScript AI library '{filename}' created successfully.")

if __name__ == "__main__":
    try:
        create_js_ai_library()
    except Exception as e:
        print("Error creating library:", e)
