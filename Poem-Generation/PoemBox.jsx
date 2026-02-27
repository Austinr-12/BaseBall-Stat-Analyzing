import { GoogleGenerativeAI } from "@google/generative-ai";
import ".env"
export default function PoemBox() {
  function fetchPoem() {
    try {
      const genAI = new GoogleGenerativeAI(API_KEY); // replace with your key
    }
  } catch (err) {
    // error handle here
  }
}
