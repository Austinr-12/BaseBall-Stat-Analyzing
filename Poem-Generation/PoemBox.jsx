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

useEffect(() => {
  // Fetch a poem on initial render
  fetchPoem();

  // Fetch a new poem every 30 seconds
  const poemIntervalId = setInterval(fetchPoem, 30000);
  return () => {
    clearInterval(poemIntervalId); // Cleanup poem interval on component unmount
  };
}, []);

return <div>{error ? <p>{error}</p> : <p>{response}</p>}</div>;