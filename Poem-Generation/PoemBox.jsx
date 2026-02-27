import { GoogleGenerativeAI } from "@google/generative-ai";
import ".env"


export default function PoemBox() {
    const [response, setResponse] = useState("");
    const [error, setError] = useState(null);
    const [currentTime, setCurrentTime] = useState(new Date());
  function fetchPoem() {
    try {
      const genAI = new GoogleGenerativeAI(API_KEY); // replace with your key
    }
  } catch (err) {
    // error handle here
  }
}
