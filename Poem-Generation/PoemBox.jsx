import { GoogleGenerativeAI } from "@google/generative-ai";
import ".env"


const fetchPoem = async () => {
  try {
    const genAI = new GoogleGenerativeAI(API_KEY);
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
    const prompt = "AI PROMPT HERE";
    const result = await model.generateContent(prompt);
    const text = result.response.text();
    setResponse(text);
  } catch (err) {
    setError(err.message);
  }
};
