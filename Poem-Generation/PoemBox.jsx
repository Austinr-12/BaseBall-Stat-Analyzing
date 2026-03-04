import { GoogleGenerativeAI } from "@google/generative-ai";
import ".env"


export default function PoemBox() {
  const [response, setResponse] = useState("");
  const [error, setError] = useState(null);
  const [currentTime, setCurrentTime] = useState(new Date());

  const fetchPoem = async () => {
    try {
      const genAI = new GoogleGenerativeAI("YOUR_API_KEY");
      const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
      const prompt =
        "write me a 10 word poem in the tone of milk and honey by rupi kaur.";
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